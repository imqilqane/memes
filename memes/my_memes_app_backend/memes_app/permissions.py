from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'you are not the owner of this meme'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
