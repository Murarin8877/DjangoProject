# Generated by Django 3.1 on 2023-05-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonOneHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Radical', models.CharField(max_length=1, null=True)),
                ('Totalstrokes', models.IntegerField(max_length=60)),
            ],
        ),
    ]
