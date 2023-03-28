from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_code = models.CharField(max_length=20)
    user_account_name = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=20)
    user_location = models.CharField(max_length=20)
    user_phone_num = models.CharField(max_length=20)
    user_contact_address = models.CharField(max_length=20)
    user_contact_address_code = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.CharField(max_length=20)
    role_parent_id = models.CharField(max_length=20)
    role_name = models.CharField(max_length=20)
    role_code = models.CharField(max_length=20)
    role_description = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'role'
        verbose_name = "角色表"
        verbose_name_plural = verbose_name

class Right(models.Model):
    id = models.AutoField(primary_key=True)
    right_id = models.CharField(max_length=20)
    right_name = models.CharField(max_length=20)
    right_code = models.CharField(max_length=20)
    right_description = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'right'
        verbose_name = "权限表"
        verbose_name_plural = verbose_name

class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_role'
        verbose_name = "用户角色表"