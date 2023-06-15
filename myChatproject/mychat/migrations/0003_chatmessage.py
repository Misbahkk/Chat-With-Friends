# Generated by Django 4.1.7 on 2023-06-13 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mychat', '0002_friend_profile_profile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('mxg_reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mxg_reciver', to='mychat.profile')),
                ('mxg_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mxg_sender', to='mychat.profile')),
            ],
        ),
    ]
