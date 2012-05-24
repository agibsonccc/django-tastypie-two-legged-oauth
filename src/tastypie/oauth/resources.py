from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User
from authentication import TwoLeggedOAuthAuthentication

class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authorization = DjangoAuthorization()
        authentication = TwoLeggedOAuthAuthentication()

