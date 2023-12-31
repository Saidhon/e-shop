# Generated by Django 4.2 on 2023-07-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_products_input_price_alter_products_sell_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productbrend",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Brend nomi"),
        ),
        migrations.AlterField(
            model_name="products",
            name="image",
            field=models.ImageField(upload_to="media", verbose_name="Maxsulot rasmi"),
        ),
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.CharField(max_length=40, verbose_name="maxsulot nomi"),
        ),
        migrations.AlterField(
            model_name="products",
            name="top_reyting",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="producttype",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Maxsulot turi"),
        ),
    ]
