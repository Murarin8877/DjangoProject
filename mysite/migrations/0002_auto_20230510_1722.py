# Generated by Django 3.1 on 2023-05-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessononehanzi',
            name='Totalstrokes',
            field=models.IntegerField(),
        ),
    ]
