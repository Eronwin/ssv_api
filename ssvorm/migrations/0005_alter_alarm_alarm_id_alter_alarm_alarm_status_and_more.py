# Generated by Django 4.1.7 on 2023-03-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ssvorm", "0004_alter_alarm_alarm_id_alter_alarm_device_alarm_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alarm",
            name="alarm_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="alarm_status",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="device_alarm_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="sensor_alarm_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="alarm",
            name="store_alarm_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_status",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_store_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_type",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="right",
            name="right_code",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="right",
            name="right_description",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="right",
            name="right_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="right",
            name="right_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="role",
            name="role_code",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="role",
            name="role_description",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="role",
            name="role_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="role",
            name="role_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="role",
            name="role_parent_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="roleright",
            name="right_type",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_device_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_status",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_type",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="sensor_value",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_desc",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_smax",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_smin",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="status",
            name="status_type",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_address",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_address_code",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_manager_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_phone_num",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_account_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_code",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_contact_address",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_contact_address_code",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_location",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_name",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_password",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_phone_num",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_sex",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="userrole",
            name="role_id",
            field=models.CharField(max_length=1024),
        ),
    ]
