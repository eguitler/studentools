from django.db import models
from django.contrib.auth.models import User


class EntityModel(models.Model):
    tag = models.CharField(max_length=10, default=None)
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=15, default=None)
    address = models.CharField(max_length=50, default=None)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    web = models.URLField(default=None)
    social_web = models.URLField(default=None)
    #image = models.ImageField(upload_to=None)


class University(EntityModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Universities'


class Faculty(EntityModel):
    university_parent = models.ForeignKey( 'University',
                                            on_delete=models.CASCADE,
                                            related_name='faculties',
                                            blank=True
                        )
    def __str__(self):
        return '{} - {}'.format(self.tag, self.name)

    class Meta:
        verbose_name_plural = 'Faculties'


class Institute(EntityModel):

    def __str__(self):
        return self.name

class School(EntityModel):

    def __str__(self):
        return self.name


# ======================================

class BaseCustomUser(User):

    # first_name
    # last_name
    # email
    # username
    # password
    birth_date = models.DateField(default=None)
    genere = models.CharField(max_length=10, default=None)
    age = models.PositiveSmallIntegerField(default=None)
    phone = models.CharField(max_length=15, default=None)
    address = models.CharField(max_length=50, default=None)
    web = models.URLField(default=None)
    social_web = models.URLField(default=None)
    #image = models.ImageField(upload_to=None)


class Teacher(BaseCustomUser):
    working_at = models.ManyToManyField( 'EntityModel',
                                         related_name='teachers',
                                         blank=True
                 )


class Student(BaseCustomUser):
    studying_at = models.ManyToManyField( 'EntityModel',
                                          related_name='students',
                                          blank=True
                  )