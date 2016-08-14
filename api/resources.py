from tastypie import fields
from tastypie.resources import ModelResource
from studentools.models import (
    University,
    Faculty,
    Institute,
    School,
    Teacher
)


class UniversityResource(ModelResource):
    class Meta:
        resource_name = 'uni'
        queryset = University.objects.all()
        allowed_methods = ['get']
        excludes = ['id']


class FacultyResource(ModelResource):
    university_parent = fields.ForeignKey(UniversityResource, 'university_parent')
    pin_color = fields.CharField(default='907bfc')
    class Meta:
        resource_name = 'fac'
        queryset = Faculty.objects.all()
        allowed_methods = ['get']
        excludes = ['id']

class InstituteResource(ModelResource):
    pin_color = fields.CharField(default='fc8d7b')
    class Meta:
        resource_name = 'ins'
        queryset = Institute.objects.all()
        allowed_methods = ['get']
        excludes = ['id']


class SchoolResource(ModelResource):
    pin_color = fields.CharField(default='90fc7b')
    class Meta:
        resource_name = 'sch'
        queryset = School.objects.all()
        allowed_methods = ['get']
        excludes = ['id']


class TeacherResource(ModelResource):
    pin_color = fields.CharField(default='fc7bbd')

    class Meta:
        resource_name = 'tea'
        queryset = Teacher.objects.all()
        allowed_methods = ['get']
        excludes = [ 'id',
                     'date_joined',
                     'last_login',
                     'first_name',
                     'last_name',
                     'email',
                     'address',
                     'age',
                     'genere',
                     'birth_date',
                     'is_active',
                     'is_staff',
                     'is_superuser',
                     'password',
                     'phone',
                     'username',
                     'web',
                     'social_web'
        ]
