"""studentools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tastypie.api import Api

from studentools.forms import SignUpForm
from studentools.views import (
    Home,
    AboutUs,
    HowWorks,
    Contact,
    Profile,
    Registration,
    Institutions
)
from api.resources import (
    UniversityResource,
    FacultyResource,
    InstituteResource,
    SchoolResource,
    TeacherResource
)

api_v1 = Api(api_name='v1')
api_v1.register(UniversityResource())
api_v1.register(FacultyResource())
api_v1.register(InstituteResource())
api_v1.register(SchoolResource())
api_v1.register(TeacherResource())

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Home
    url(r'^$', Home.as_view(), name='home'),
    # Links
    url(r'^QuienesSomos/', AboutUs.as_view()),
    url(r'^ComoFunciona/', HowWorks.as_view()),
    url(r'^Contacto/', Contact.as_view()),
    # Manage Account
    url(r'^accounts/profile/', Profile.as_view()),
    url(r'^accounts/register/', Registration.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # Institutions
    url(r'^institutions/', Institutions.as_view()),

    # Api
    url(r'^api/', include(api_v1.urls)),
] + staticfiles_urlpatterns()
