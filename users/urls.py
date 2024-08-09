from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from users import views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), #
    path('logout/', LogoutView.as_view(template_name='apps/index.html'), name="logout"), #
    path('register/', views.register, name='register'), #
    path('edit_profile/', views.edit_profile, name='edit_profile'), #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)