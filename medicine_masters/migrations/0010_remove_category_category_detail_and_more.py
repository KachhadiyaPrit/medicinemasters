# Generated by Django 5.0 on 2023-12-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0009_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_detail',
        ),
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]
