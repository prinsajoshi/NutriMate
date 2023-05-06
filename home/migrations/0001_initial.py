# Generated by Django 4.1.7 on 2023-05-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('ingredients', models.TextField()),
                ('meal_link', models.TextField()),
                ('recipe', models.TextField()),
            ],
        ),
    ]
