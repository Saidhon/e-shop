# Generated by Django 4.2 on 2023-05-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_specialproduct_topproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizgaYoqishiMumkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turi', models.CharField(max_length=90)),
                ('nomi', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
    ]