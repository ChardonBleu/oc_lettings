# Generated by Django 3.0 on 2021-11-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0002_auto_20211128_2152"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]