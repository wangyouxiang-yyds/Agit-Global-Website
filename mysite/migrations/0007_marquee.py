# Generated by Django 4.2.4 on 2023-09-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0006_common_link_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="marquee",
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
                ("display_or_not", models.BooleanField(verbose_name="是否要顯示")),
                ("announcement", models.CharField(max_length=100, verbose_name="公告文字")),
                (
                    "modify_date",
                    models.DateTimeField(auto_now=True, verbose_name="修改時間"),
                ),
                ("modify_user", models.CharField(max_length=50, verbose_name="修改者")),
            ],
        ),
    ]