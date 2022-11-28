from rest_framework import serializers
from webapp.models import Leads, Course, EducationalMaterials, Profile, User


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ['name', 'phone']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EducationalMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterials
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'