# Generated by Django 4.0.1 on 2022-06-24 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0004_soundhistory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="soundhistory",
            old_name="command",
            new_name="sound",
        ),
    ]
