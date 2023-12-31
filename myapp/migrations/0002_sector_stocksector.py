# Generated by Django 4.2.2 on 2023-06-28 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sector",
            fields=[
                (
                    "ID",
                    models.IntegerField(
                        db_column="ID", primary_key=True, serialize=False
                    ),
                ),
                ("SecGrpID", models.IntegerField()),
                ("SectorName", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "sector",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StockSector",
            fields=[
                (
                    "StockID",
                    models.OneToOneField(
                        db_column="StockID",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="myapp.stock",
                    ),
                ),
                ("SectorID", models.IntegerField()),
            ],
            options={
                "db_table": "stock_sector",
                "managed": False,
            },
        ),
    ]
