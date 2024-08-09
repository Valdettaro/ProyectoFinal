from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index.html', views.home, name='home'), #
    path('index.html', views.home, name='index'), #
    path('about.html', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), #
    path('pricing.html', views.pricing, name='pricing'),
    path('rate/', views.rate_website, name='rate'), #
    path('search_ratings/', views.search_ratings, name='search_ratings'),
    path('faq.html', views.faq, name='faq'), 
    path('materiales/', views.materiales, name='materiales'), #
    path('search-email/', views.search_email, name='search_email'), #
    path('productos/', views.productos, name='productos'),
    path('acrilico-crystal/', views.acrilico_crystal, name='acrilico_crystal'),
    path('acrilico-gliiter/', views.acrilico_glitter, name='acrilico_glitter'),
    path('acrilico-color/', views.acrilico_color, name='acrilico_color'),
    path('acrilico-espejo/', views.acrilico_espejo, name='acrilico_espejo'),
    path('materiales/edit/<int:id>/', views.edit_material, name='edit_material'),
    path('materiales/delete/<int:id>/', views.delete_material, name='delete_material'),
    path('chat/', views.chat_room, name='chat_room'),
    path('send_message/', views.send_message, name='send_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('forum/', views.forum, name='forum'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('subscribe/', views.newsletter_subscription, name='newsletter_subscription'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)