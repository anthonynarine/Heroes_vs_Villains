# Generated by Django 4.1.2 on 2022-10-22 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("super_types", "0004_remove_supertype_super_type"),
        ("supers", "0003_super_super_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="super",
            name="super_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="super_types.supertype",
            ),
            preserve_default=False,
        ),
    ]
