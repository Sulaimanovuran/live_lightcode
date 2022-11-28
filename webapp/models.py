from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser, BaseUserManager):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

    def __str__(self):
        return "{}".format(self.username)

    STUDENT = 'STUDENT'
    MENTOR = 'MENTOR'
    ROLES = (
        (MENTOR, 'MENTOR'),
        (STUDENT, 'STUDENT'),
    )
    role = models.CharField(choices=ROLES, max_length=128)

    @property
    def is_mentor(self):
        return self.role == self.MENTOR

    @property
    def is_student(self):
        return self.role == self.STUDENT

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh),
                'access': str(refresh.access_token)}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True)
    phone_number = models.CharField(max_length=128, null=True)
    photo = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

    def __str__(self):
        return self.user.email


class Course(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=None)
    author = models.CharField(max_length=100, null=True)
    discount = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def __str__(self):
        return self.name


class Leads(models.Model):
    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name_plural = 'Потенциальные клиенты'
        verbose_name = 'Потенциальный клиент'

    def __str__(self):
        return self.name


class EducationalMaterials(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_material')
    description = models.TextField()
    link = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name_plural = 'Учебные материалы'
        verbose_name = 'Учебный материал'

    def __str__(self):
        return self.course






