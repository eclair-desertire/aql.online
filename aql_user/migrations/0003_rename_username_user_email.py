# Generated by Django 4.0 on 2022-11-17 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aql_user', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
    ]