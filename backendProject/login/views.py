from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from rest_framework.response import Response

from rest_framework import generics
from . import models
from . import serializers


from rest_framework.permissions import IsAuthenticated
from login.models import Category, ItemCategory
from login.serializers import CategorySerializer, ItemCategorySerializer 
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


class ListTodo(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = models.Todo.objects.all()
        serializer_class = serializers.TodoSerializer
        return Response("hola jose desde el metodo get")

@csrf_exempt
@api_view(["GET"])
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

@permission_classes((AllowAny,))
class CategoryList (generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
@permission_classes((AllowAny,))
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
@permission_classes((AllowAny,))
class ItemCategoryList(generics.ListCreateAPIView):
    queryset = models.ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
@permission_classes((AllowAny,))
class ItemCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer