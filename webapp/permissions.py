from rest_framework import permissions

#
# class IsAdmin(BasePermission):
#
#     def has_permission(self, request, view):
#         if request.user.is_anonymous:
#             return False
#         else:
#             return bool(request.user and request.user.is_admin)
#
#
# class IsAdminOrProjectManager(BasePermission):
#
#     def has_permission(self, request, view):
#         # print(request.user.role)
#         if request.user.is_anonymous:
#             return False
#         # if request.user:
#         #     return bool(request.user and request.user.is_admin or request.user.is_project_manager)
#         else:
#             return bool(request.user and request.user.is_admin or request.user.is_project_manager)



class IsAuthenticatedProfile(permissions.BasePermission): # Аунтифицированные пользователи видят только свои профели, и могут длеать что хотят

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthenticatedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsLoggedInUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class IsAdminUser(permissions.BasePermission):  #Только Админ имеет право удалять User

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsAdminOrMentor(permissions.BasePermission):  #Ментор или Админ имеет право создавать курсы

    def has_permission(self, request, view):
        return request.user and request.user.is_mentor

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_mentor

