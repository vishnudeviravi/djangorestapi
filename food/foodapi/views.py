from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import FoodSerializer
from .models import Food
from rest_framework.response import Response

# Create your views here.


class FoodList(APIView):

    def get(self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

    # def post(self,request):
