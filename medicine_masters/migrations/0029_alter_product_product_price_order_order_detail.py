# Generated by Django 5.0 on 2023-12-26 11:59

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0028_alter_users_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('order_total_amount', models.CharField(max_length=150)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('order_detail_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150, null=True)),
                ('product_quantity', models.CharField(max_length=150, null=True)),
                ('product_price', models.CharField(max_length=150, null=True)),
                ('total_price', models.CharField(max_length=150, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_masters.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_masters.product')),
            ],
        ),
    ]
