from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home .models import  (Animal)
from home .serializers import AnimalSerializer
# Create your views here.


class AnimalView(APIView):
    
    def get(self ,request):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many =True)
        return Response({'status':True , ",message":"animal Fectched with get" ,"data":serializer.data})
    
    def post(self , request):
        return Response({'status':True , ",message":"animal Fectched post"  })
    
    def put(self , request):
        return Response({'status':True , ",message":"animal Fectched put"  })
    
    def patch(self , request):
        return Response({'status':True , ",message":"animal Fectched delete" })