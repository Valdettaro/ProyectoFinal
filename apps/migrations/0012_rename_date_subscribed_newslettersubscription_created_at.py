# Generated by Django 4.2 on 2024-08-06 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_newslettersubscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newslettersubscription',
            old_name='date_subscribed',
            new_name='created_at',
        ),
    ]
