from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import FAQ
from .serializer import FAQSerializer


# Create your views here.

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang','en')
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs,many=True,context={'lang': lang})
        return Response(serializer.data)


class FAQCreateView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
