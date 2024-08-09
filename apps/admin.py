from django.contrib import admin
from apps.models import Contact, Materiales, Rating, NewsletterSubscription

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')  # columnsa
    search_fields = ('name', 'email')   # busqueda
    list_filter = ('created_at',)  # filtro

class MaterialesAdmin(admin.ModelAdmin):
    list_display = ('material', 'color')
    search_fields = ('material', 'color')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'created_at')  
    list_filter = ('rating',)  
    search_fields = ('comment',) 
    ordering = ('-created_at',)  # prueba ordenar

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Materiales, MaterialesAdmin)
admin.site.register(Rating, RatingAdmin)


