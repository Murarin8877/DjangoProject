# Generated by Django 3.1 on 2023-05-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonOneHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=20)),
                ('Radical', models.CharField(max_length=1, null=True)),
                ('Total_strokes', models.IntegerField(max_length=60)),
            ],
        ),
    ]
