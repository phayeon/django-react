# Generated by Django 4.1 on 2022-12-27 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('shop_users', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deliveries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.deliveries')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('shop_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_users.shop_user')),
            ],
            options={
                'db_table': 'shop_orders',
            },
        ),
    ]
