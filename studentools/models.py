from django.db import models
from django.contrib.auth.models import User


class BaseCustomUser(User):
    pass


class HumanUser(BaseCustomUser):
    pass


class EntityUser(BaseCustomUser):
    pass


class Institution(EntityUser):
    pass


class Headquarter(EntityUser):
    pass


class Teacher(HumanUser):
    pass


class Student(HumanUser):
    pass
