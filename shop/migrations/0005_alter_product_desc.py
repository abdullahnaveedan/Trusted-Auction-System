# Generated by Django 4.1.3 on 2023-06-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_product_useremail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="desc",
            field=models.CharField(max_length=600),
        ),
    ]
