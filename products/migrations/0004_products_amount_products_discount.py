# Generated by Django 4.2 on 2023-07-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_productbrend_name_alter_products_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="amount",
            field=models.IntegerField(default=0, verbose_name="maxsulot miqdori"),
        ),
        migrations.AddField(
            model_name="products",
            name="discount",
            field=models.IntegerField(default=0, verbose_name="maxsulot chegirmasi"),
        ),
    ]
