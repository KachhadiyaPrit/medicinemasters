# Generated by Django 5.0 on 2023-12-24 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0022_alter_users_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_contact_person',
            new_name='company_owner',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_contact_email',
            new_name='company_owner_email',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_contact_phone',
            new_name='company_owner_phone',
        ),
    ]
