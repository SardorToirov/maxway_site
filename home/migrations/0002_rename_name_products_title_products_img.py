# Generated by Django 5.1.7 on 2025-03-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, default='images/img.png', null=True, upload_to='images'),
        ),
    ]
