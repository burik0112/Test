from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import TimeSheet



class TimeSheetSerializer(ModelSerializer):
    class Meta:
        model = TimeSheet
        fields = '__all__'