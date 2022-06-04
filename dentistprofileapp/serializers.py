from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from dentistprofileapp.models import Registration

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegistrationSerializer, self).create(validated_data)

class ViewRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"