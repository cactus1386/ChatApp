# Generated by Django 4.2.5 on 2024-12-20 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_rename_chat_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]
