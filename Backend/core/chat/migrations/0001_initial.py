# Generated by Django 4.2.5 on 2024-12-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
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
                ("user", models.CharField(max_length=20)),
                ("massage", models.TextField()),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
