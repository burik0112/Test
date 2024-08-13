from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import TimeSheet
from user.serializers import TimeSheetSerializer


class TimeSheetAPIView(APIView):

    def get(self, request):
        items = TimeSheet.objects.all()
        serializer = TimeSheetSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = TimeSheetSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
