from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account  # Make sure your Account model is imported correctly
from .serializers import AccountSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer