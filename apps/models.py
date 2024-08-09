from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  #implementa la hora en la que se crea el mensaje, necesita importar libreria

    def __str__(self):
        return self.name

class Materiales(models.Model):
    material = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.material

class Rating(models.Model):
    rating = models.PositiveIntegerField(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 11)], default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.rating} Stars'

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email