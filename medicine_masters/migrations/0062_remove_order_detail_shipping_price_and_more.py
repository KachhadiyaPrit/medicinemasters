# Generated by Django 5.0.1 on 2024-01-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0061_order_detail_user_alter_order_detail_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='shipping_price',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_price',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order confirmed', 'Order confirmed'), ('Picked by courier', 'Picked by courier'), ('On the way', 'On the way'), ('Ready for pickup', 'Ready for pickup'), ('Order Received', 'Order Received')], default='Order confirmed', max_length=100),
        ),
    ]
