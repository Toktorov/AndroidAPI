from rest_framework import serializers
from contact_form.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = "__all__"