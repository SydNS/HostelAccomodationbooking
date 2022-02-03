from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Useraccountsmodel(BaseUserManager):
    email = models.EmailField(unique=True)
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an email")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, verbose_name="date_joined")
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    # profileimage=models.ImageField(max_length=255,upload_to=,null=True,default=)

    objects = Useraccountsmodel()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.username

    def has_module_perms(self, app_label):
        return True


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    YEAR = [
        ('FIRST_YEAR', 'FIRST_YEAR'),
        ('SECOND_YEAR', 'SECOND_YEAR'),
        ('THIRD_YEAR', 'THIRD_YEAR'),
        ('FORTH_YEAR', 'FORTH_YEAR'),
    ]

    name_user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=6)
    photo = models.ImageField(upload_to='profileimages/')
    phonenumber = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=200)
    parent_phonenumber = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    reporting_date = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    studentIdnumber = models.CharField(max_length=10)
    level_of_study = models.CharField(max_length=11, choices=YEAR)
    # photo_img = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Student Accounts"


    def __str__(self):
        return str(self.name_user)
