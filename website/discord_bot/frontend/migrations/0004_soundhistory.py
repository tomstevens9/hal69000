# Generated by Django 4.0.1 on 2022-06-24 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.DateTimeField(auto_now_add=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.sound')),
            ],
        ),
    ]
