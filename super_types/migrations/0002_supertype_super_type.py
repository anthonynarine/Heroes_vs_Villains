# Generated by Django 4.1.2 on 2022-10-22 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("supers", "0002_remove_super_super_type"),
        ("super_types", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="supertype",
            name="super_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="supers.super",
            ),
        ),
    ]