# Generated by Django 5.0.6 on 2024-05-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_no", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("genre", models.CharField(max_length=100)),
            ],
        ),
    ]