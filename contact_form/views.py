from django.shortcuts import render
from contact_form.serializers import ContactSerializer
from contact_form.models import Contact
from rest_framework import generics

# Create your views here.
class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CreateContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer