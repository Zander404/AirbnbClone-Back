# Generated by Django 5.0.6 on 2024-06-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='send_to',
            new_name='sent_to_id',
        ),
    ]
