# Generated by Django 5.0 on 2023-12-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0008_alter_users_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=150, unique=True)),
                ('category_detail', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
