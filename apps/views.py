from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Contact, Materiales, Rating, Message, Post, NewsletterSubscription
from .forms import ContactForm, MaterialesForm, SearchMaterialForm, SearchEmailForm, RatingForm, SearchRatingForm, MessageForm, PostForm, NewsletterForm
import csv

def home(request):
    return render(request, "apps/index.html")

def about(request):
    return render(request, "apps/about.html")

def pricing(request):
    return render(request, "apps/pricing.html")

def faq(request):
    return render(request, "apps/faq.html")

def home(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if NewsletterSubscription.objects.filter(email=email).exists():
                messages.error(request, 'El email ya está registrado.')
            else:
                form.save()
                messages.success(request, 'Suscripción realizada con éxito.')
            return redirect('index')
    else:
        form = NewsletterForm()

    return render(request, 'apps/index.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('home') 
    else:
        form = ContactForm()
    
    return render(request, 'apps/contact.html', {'form': form})

def materiales(request):
    if request.method == 'POST':
        form = MaterialesForm(request.POST)
        if form.is_valid():
            Materiales.objects.create(
                material=form.cleaned_data['material'],
                color=form.cleaned_data['color'],
            )
            return redirect('materiales')
    else:
        form = MaterialesForm()
    
    search_form = SearchMaterialForm(request.GET or None)
    if search_form.is_valid() and 'color' in request.GET:
        color = search_form.cleaned_data['color']
        materiales = Materiales.objects.filter(color__icontains=color)
    else:
        materiales = Materiales.objects.all()
    
    return render(request, 'apps/materiales.html', {
        'form': form,
        'search_form': search_form,
        'materiales': materiales
    })

def edit_material(request, id):
    material = get_object_or_404(Materiales, id=id)
    if request.method == 'POST':
        form = MaterialesForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materiales')
    else:
        form = MaterialesForm(instance=material)
    
    return render(request, 'apps/edit_material.html', {'form': form, 'material': material})

def delete_material(request, id):
    material = get_object_or_404(Materiales, id=id)
    if request.method == 'POST':
        material.delete()
        return redirect('materiales')
    
    return render(request, 'apps/delete_material.html', {'material': material})

def search_email(request):
    form = SearchEmailForm(request.GET or None)
    users = []
    search_made = False #elimina el resultado de busqueda al inicio

    if form.is_valid():
        email = form.cleaned_data.get('email')
        users = User.objects.filter(email=email).values('id', 'username', 'first_name', 'last_name', 'email')
        search_made = True 

    return render(request, 'apps/search_email.html', {'form': form, 'users': users, 'search_made': search_made})

def rate_website(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gracias por tu calificación')
            return redirect('rate')
    else:
        form = RatingForm()

    return render(request, 'apps/rate.html', {'form': form})

def search_ratings(request):
    form = SearchRatingForm(request.GET or None)
    ratings = []
    search_made = False
    average_rating = None

    if form.is_valid():
        stars = form.cleaned_data.get('stars')
        ratings = Rating.objects.filter(rating=stars)
        search_made = True
        
        average_rating = Rating.objects.aggregate(average_rating=Avg('rating'))['average_rating'] #revisar si esta calculando bien el promedio

    return render(request, 'apps/search_ratings.html', {
        'form': form,
        'ratings': ratings,
        'search_made': search_made,
        'average_rating': average_rating
    })

def productos(request):
    return render(request, "apps/productos.html")

def acrilico_crystal(request):
    return render(request, "apps/acrilico_crystal.html")

def acrilico_glitter(request):
    return render(request, "apps/acrilico_glitter.html")

def acrilico_color(request):
    return render(request, "apps/acrilico_color.html")

def acrilico_espejo(request):
    return render(request, "apps/acrilico_espejo.html")

@login_required
def chat_room(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat_room')
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'apps/chat_room.html', {'form': form, 'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return JsonResponse({'message': message.content, 'user': message.user.username})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('chat_room')  # Redirige a la sala de chat o a donde quieras

@login_required
def forum(request):
    posts = Post.objects.all().order_by('-timestamp')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum')
    else:
        form = PostForm()
    return render(request, 'apps/forum.html', {'posts': posts, 'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.user and not request.user.is_superuser:
        return redirect('forum')  # Redirect if the user is not authorized

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('forum')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'apps/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.user and not request.user.is_superuser:
        return redirect('forum')  # Redirect if the user is not authorized

    if request.method == 'POST':
        post.delete()
        return redirect('forum')
    
    return render(request, 'apps/delete_post.html', {'post': post})

def newsletter_subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado.')
        else:
            NewsletterSubscription.objects.create(email=email)
            messages.success(request, 'Te has suscrito exitosamente al boletín.')
    return redirect('index')