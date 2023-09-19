# Generated by Django 4.2.4 on 2023-08-31 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="manager_category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manager_category", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="manager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manager_name", models.CharField(max_length=10)),
                ("position", models.CharField(max_length=10)),
                (
                    "manager_photo",
                    models.ImageField(max_length=255, upload_to="manager_photo"),
                ),
                ("manager_saying", models.CharField(max_length=50)),
                (
                    "manager_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mysite.manager_category",
                    ),
                ),
            ],
        ),
    ]
