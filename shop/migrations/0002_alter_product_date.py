# Generated by Django 4.1.3 on 2023-06-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
