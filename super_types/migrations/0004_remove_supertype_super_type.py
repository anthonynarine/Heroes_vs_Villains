# Generated by Django 4.1.2 on 2022-10-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("super_types", "0003_alter_supertype_super_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supertype",
            name="super_type",
        ),
    ]
