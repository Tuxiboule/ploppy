from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, MissionSerializer, EstimateSerializer, InvoiceSerializer
from .models import Customer, Mission, Estimate, Invoice


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class MissionView(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()


class EstimateView(viewsets.ModelViewSet):
    serializer_class = EstimateSerializer
    queryset = Estimate.objects.all()


class InvoiceView(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer()
    queryset = Invoice.objects.all()