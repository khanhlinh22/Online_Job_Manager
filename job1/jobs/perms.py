from rest_framework import permissions

class OwnerPerms(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, instance):
        return super().has_permission(request,view) and request.user == instance.user

 # custom permission đảm bảo chỉ người sở hữu mới được thao tác
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user