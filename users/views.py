from logging import exception
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from users.models import Users
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        # check if the required data is passed
        if not name or not email or not password:
            return (Response({'error': "name, pasword and email are required"}))
        
        # check if user already exist before creating new one
        user = Users.objects.filter(email=email).exists()
        if user:
            return (Response({'error': "User already exist"}, status=status.HTTP_201_CREATED))

        newUser = Users(name=name, email=email, password=password)
        newUser.save()
    
        newUser.save()
        return(Response({'message': 'success', 'data': {'name': name, 'email': email}}))
        
    except Exception as e:
        print(e, 'error')
        return(Response({'error: ', "error registering user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR))
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': "Email and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            return Response({'error': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message': "✅ Login successful!", 'user': {'name': user.name, 'email': user.email}}, status=status.HTTP_200_OK)
    
    except Exception as e:
        print(f"Error during login: {e}")
        return Response({'error': "Login failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
    try:
        users = Users.objects.all().values("id", "name", "email")  
        return Response({"users": list(users)}, status=status.HTTP_200_OK) 
    except Exception as e:
        return Response({"error": f"Error fetching users: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, user_id):
    try:
        print(user_id, 'user_id')
        user = get_object_or_404(Users, id=user_id)
        print(user, 'user====')
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': f'Error deleting user: {str(e)}'}, status=500)