from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=1024)
    user_name = models.CharField(max_length=1024)
    user_password = models.CharField(max_length=1024)
    user_code = models.CharField(max_length=1024)
    user_account_name = models.CharField(max_length=1024)
    user_sex = models.CharField(max_length=1024)
    user_location = models.CharField(max_length=1024)
    user_phone_num = models.CharField(max_length=1024)
    user_contact_address = models.CharField(max_length=1024)
    user_contact_address_code = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

# 角色表
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.CharField(max_length=1024)
    role_parent_id = models.CharField(max_length=1024)
    role_name = models.CharField(max_length=1024)
    role_code = models.CharField(max_length=1024)
    role_description = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'role'
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
# 权限表
class Right(models.Model):
    id = models.AutoField(primary_key=True)
    right_id = models.CharField(max_length=1024)
    right_name = models.CharField(max_length=1024)
    right_code = models.CharField(max_length=1024)
    right_description = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'right'
        verbose_name = "权限表"
        verbose_name_plural = verbose_name
# 用户角色表
class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_role'
        verbose_name = "用户角色表"
# 角色权限表
class RoleRight(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.OneToOneField(Role, on_delete=models.CASCADE)
    right_id = models.OneToOneField(Right, on_delete=models.CASCADE)
    right_type = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
# 门店表
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=1024)
    store_name = models.CharField(max_length=1024)
    store_manager_id = models.CharField(max_length=1024)
    store_address = models.CharField(max_length=1024)
    store_address_code = models.CharField(max_length=1024)
    store_phone_num = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
# 设备表
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=1024)
    device_name = models.CharField(max_length=1024)
    device_type = models.CharField(max_length=1024)
    device_status = models.CharField(max_length=1024)
    device_store_id = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

# 传感器表
class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_id = models.CharField(max_length=1024)
    sensor_name = models.CharField(max_length=1024)
    sensor_type = models.CharField(max_length=1024)
    sensor_status = models.CharField(max_length=1024)
    sensor_value = models.CharField(max_length=1024)
    sensor_device_id = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

# 状态表
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status_id = models.CharField(max_length=1024)
    status_name = models.CharField(max_length=1024)
    status_type = models.CharField(max_length=1024)
    status_smax = models.CharField(max_length=1024)
    status_smin = models.CharField(max_length=1024)
    status_desc = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

# 警报表
class Alarm(models.Model):
    id = models.AutoField(primary_key=True)
    alarm_id = models.CharField(max_length=1024)
    store_alarm_id = models.CharField(max_length=1024)
    device_alarm_id = models.CharField(max_length=1024)
    sensor_alarm_id = models.CharField(max_length=1024)
    alarm_desc = models.CharField(max_length=128)
    alarm_status = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

