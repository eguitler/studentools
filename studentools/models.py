from django.db import models
from django.contrib.auth.models import User


class EntityModel(models.Model):
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=15, default=None)
    address = models.CharField(max_length=50, default=None)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    web = models.URLField(default=None)
    social_web = models.URLField(default=None)
    #image = models.ImageField(upload_to=None)

    def __str__(self):
        try:
            return '{} - {}'.format(self.university_parent.tag, self.name)
        except AttributeError:
            return self.name

class University(models.Model):
    tag = models.CharField(max_length=10, default=None)
    name = models.CharField(max_length=50, default=None)
    #image = models.ImageField(upload_to=None)

    def __str__(self):
        return '{} - {}'.format(self.tag, self.name)

    class Meta:
        verbose_name_plural = 'Universities'


class Faculty(EntityModel):
    university_parent = models.ForeignKey( 'University',
                                            on_delete=models.CASCADE,
                                            related_name='faculties',
                                            null=True,
                                            blank=True
                        )

    class Meta:
        verbose_name_plural = 'Faculties'


class Institute(EntityModel):
    pass


class School(EntityModel):
    pass


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
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    web = models.URLField(default=None)
    social_web = models.URLField(default=None)
    #image = models.ImageField(upload_to=None)


class Teacher(BaseCustomUser):
    working_at = models.ManyToManyField( 'EntityModel',
                                         related_name='teachers',
                                         blank=True
                 )
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Student(BaseCustomUser):
    studying_at = models.ManyToManyField( 'EntityModel',
                                          related_name='students',
                                          blank=True
                  )