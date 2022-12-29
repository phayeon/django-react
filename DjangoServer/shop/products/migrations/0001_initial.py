# Generated by Django 4.1 on 2022-12-29 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('image_url', models.TextField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categories')),
            ],
            options={
                'db_table': 'shop_product',
            },
        ),
    ]
