# Generated by Django 4.2.10 on 2024-03-06 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('about', djrichtextfield.models.RichTextField(max_length=10000)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='user_profiles/')),
                ('profile_type', models.CharField(choices=[('instructor', 'Instructor'), ('therapist', 'Therapist')], default='instructor', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_name'],
            },
        ),
    ]