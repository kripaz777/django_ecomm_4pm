# Generated by Django 4.2.2 on 2023-07-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_brand_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(default="", max_length=500),
        ),
    ]