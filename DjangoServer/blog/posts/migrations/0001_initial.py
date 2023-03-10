# Generated by Django 4.1 on 2022-12-29 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_users.bloguser')),
            ],
            options={
                'db_table': 'blog_post',
            },
        ),
    ]
