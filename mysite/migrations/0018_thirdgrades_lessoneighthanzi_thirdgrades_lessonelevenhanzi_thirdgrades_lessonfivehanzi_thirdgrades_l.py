# Generated by Django 3.1 on 2023-05-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20230513_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdgradeS_LessonEightHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonElevenHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonFiveHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonFourHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonNineHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonOneHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonSevenHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonSixHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonTenHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonThreeHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonTwelveHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdgradeS_LessonTwoHanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hanzi', models.CharField(max_length=1)),
                ('Bopomofo', models.CharField(max_length=25)),
                ('Radical', models.CharField(blank=True, max_length=1, null=True)),
                ('R_Bopomofo', models.CharField(blank=True, max_length=10, null=True)),
                ('Total_strokes', models.IntegerField()),
            ],
        ),
    ]