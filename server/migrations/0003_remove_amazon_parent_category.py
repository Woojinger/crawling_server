# Generated by Django 3.0.4 on 2020-03-16 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_amazon_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazon',
            name='Parent_category',
        ),
    ]