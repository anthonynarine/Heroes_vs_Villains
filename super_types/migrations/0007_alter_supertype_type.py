# Generated by Django 4.1.2 on 2022-10-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("super_types", "0006_remove_supertype_hero_remove_supertype_villain_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supertype",
            name="type",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
