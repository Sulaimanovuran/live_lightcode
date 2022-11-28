from django.urls import path, include

from webapp.views import LeadsViewSet, CourseViewSet, ProfileViewSet, EducationalMaterialsViewSet, UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('leads/', LeadsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('lead/<int:pk>/', LeadsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('educational_materials/', EducationalMaterialsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('educational_material/<int:pk>/', EducationalMaterialsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
  #  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]