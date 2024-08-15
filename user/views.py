from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from drf_yasg import openapi
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import TimeSheet
from user.serializers import TimeSheetSerializer
from rest_framework.parsers import JSONParser, MultiPartParser


class TimeSheetAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser, MultiPartParser]

    @extend_schema(
        request=TimeSheetSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: TimeSheetSerializer(many=True)},
        tags=['Time'],
        methods=['GET'],
        operation_id='Time_get'
    )
    def get(self, request, pk: str = None):
        if pk:
            obj = get_object_or_404(TimeSheet, pk=pk)
            serializer = TimeSheetSerializer(obj)
            return Response({'Volunteer': serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        serializer = TimeSheetSerializer(TimeSheet.objects.all(), many=True)
        return Response({"Response": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=TimeSheetSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: TimeSheetSerializer(many=True)},
        tags=['Time'],
        methods=['POST'],
        operation_id='Time_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = TimeSheetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Volunteer has been saved": serializer.data}, status=status.HTTP_201_CREATED,
                            content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST,
                        content_type='application/json')

    @extend_schema(
        request=TimeSheetSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: TimeSheetSerializer(many=True)},
        tags=['Time'],
        methods=['PUT'],
        operation_id='Time_put'
    )
    def put(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(TimeSheet.objects.all(), pk=pk)
        serializer = TimeSheetSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST,
                        content_type='application/json')

    @extend_schema(
        request=TimeSheetSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: TimeSheetSerializer(many=True)},
        tags=['Time'],
        methods=['DELETE'],
        operation_id='Time_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(TimeSheet, pk=pk)
        obj.delete()
        return Response({"Object is deleted":'success'}, status=status.HTTP_200_OK,
                        content_type='application/json')
