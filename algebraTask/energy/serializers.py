from rest_framework import serializers
from .models import Country, Location, Users, Projects, Devices, Data_returned, Projects_user, Projects_device, projects_location

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

class DataReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_returned
        fields = '__all__'

class ProjectsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects_user
        fields = '__all__'

class ProjectsDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects_device
        fields = '__all__'

class ProjectsLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects_location
        fields = '__all__'
