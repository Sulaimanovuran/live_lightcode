from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from webapp.models import Leads, Course, EducationalMaterials, Profile, User
# from webapp.permissions import IsAdmin, IsAdminOrProjectManager
from webapp.serializers import LeadsSerializer, CourseSerializer, EducationalMaterialsSerializer, ProfileSerializer, \
    UserSerializer
from webapp.permissions import IsAuthenticatedProfile,IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrMentor


class UserViewSet(viewsets.ModelViewSet):
    """Список пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated | IsAdminUser]
        return [permission() for permission in permission_classes]


class LeadsViewSet(viewsets.ModelViewSet):
    """Список потенциальных клиентов"""
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class EducationalMaterialsViewSet(viewsets.ModelViewSet):
    """Список учебных материалов"""
    queryset = EducationalMaterials.objects.all()
    serializer_class = EducationalMaterialsSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAuthenticated | IsAdminOrMentor]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated | IsAdminOrMentor]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class ProfileViewSet(viewsets.ModelViewSet):
    """Список профилей"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedProfile]


class CourseViewSet(viewsets.ModelViewSet):
    """Список курсов"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAuthenticated | IsAdminOrMentor]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated | IsAdminOrMentor]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]