# Generated by Django 4.0.6 on 2022-07-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0004_remove_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('video', models.URLField()),
            ],
        ),
    ]