# Generated by Django 3.2.7 on 2021-09-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='legenda',
            field=models.TextField(blank=True, max_length=145, null=True),
        ),
    ]
