# Generated by Django 4.2.2 on 2023-06-22 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_cofinexport_options_alter_findata_options"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="cofinexport",
            table="cofinexport",
        ),
        migrations.AlterModelTable(
            name="findata",
            table="findata",
        ),
    ]
