from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

User = get_user_model()

@api_view(['GET'])
def list_users(request):
    if not request.user.is_admin:
        return Response(status=status.HTTP_403_FORBIDDEN)
    users = User.objects.all().values('id', 'username', 'first_name', 'email', 'is_admin')
    return Response(list(users), status=status.HTTP_200_OK)

@api_view(['POST'])
def update_user_admin_status(request, user_id):
    if not request.user.is_admin:
        return Response(status=status.HTTP_403_FORBIDDEN)
    try:
        user = User.objects.get(id=user_id)
        user.is_admin = request.data.get('is_admin', user.is_admin)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request, user_id):
    if not request.user.is_admin:
        return Response(status=status.HTTP_403_FORBIDDEN)
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
