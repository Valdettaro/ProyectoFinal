from django import forms
from .models import Rating, Materiales, Message, Post, NewsletterSubscription

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=30, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class MaterialesForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = ['material', 'color']

class SearchMaterialForm(forms.Form):
    color = forms.CharField(max_length=20, required=True, label='Buscar por color')

class SearchEmailForm(forms.Form):
    email = forms.EmailField()
    

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect,
            'comment': forms.Textarea(),
        }

class SearchRatingForm(forms.Form):
    stars = forms.ChoiceField(
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        required=True
    )

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address...'})
        }