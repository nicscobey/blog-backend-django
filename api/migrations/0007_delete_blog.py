# Generated by Django 4.0.1 on 2022-01-13 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_blog_created_at_alter_blog_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
