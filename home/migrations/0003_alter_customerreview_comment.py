# Generated by Django 4.2.2 on 2023-06-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_customerreview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerreview",
            name="comment",
            field=models.TextField(blank=True),
        ),
    ]
