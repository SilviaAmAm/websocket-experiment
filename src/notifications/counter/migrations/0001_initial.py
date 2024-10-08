# Generated by Django 5.0.7 on 2024-07-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GlobalCounter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="The value of the global counter",
                        verbose_name="count",
                    ),
                ),
            ],
            options={
                "verbose_name": "Global counter",
            },
        ),
    ]
