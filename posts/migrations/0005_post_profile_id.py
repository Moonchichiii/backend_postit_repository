# Generated by Django 5.0.1 on 2024-01-23 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_published'),
        ('profiles', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='profiles.profile'),
            preserve_default=False,
        ),
    ]
