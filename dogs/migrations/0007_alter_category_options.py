# Generated by Django 4.0 on 2024-01-10 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0006_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': [('can_view_name', 'Can view name'), ('can_change_description', 'Can change description'), ('can_view_category', 'Can view category')], 'verbose_name': 'Порода', 'verbose_name_plural': 'Породы'},
        ),
    ]
