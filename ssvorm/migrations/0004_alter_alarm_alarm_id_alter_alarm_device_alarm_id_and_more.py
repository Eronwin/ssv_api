# Generated by Django 4.1.7 on 2023-03-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ssvorm", "0003_alarm_delete_test_alter_device_device_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alarm",
            name="alarm_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="device_alarm_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="sensor_alarm_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="store_alarm_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_manager_id",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(max_length=256),
        ),
    ]
