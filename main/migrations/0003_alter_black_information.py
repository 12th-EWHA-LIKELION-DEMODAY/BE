# Generated by Django 4.2.7 on 2024-12-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_black_frame_alter_white_frame"),
    ]

    operations = [
        migrations.AlterField(
            model_name="black",
            name="information",
            field=models.TextField(blank=True, null=True),
        ),
    ]