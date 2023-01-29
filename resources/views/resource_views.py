from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers import ResourceSerializer
from ..models import Resource
from ..permissions import MasterPermission, UserEditDeletePermission


# Create your views here.
class ResourceView(APIView):
    permission_classes = [IsAuthenticated, MasterPermission]
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourceDetailView(APIView):
    permission_classes = [UserEditDeletePermission]

    def get_resource(self, id):
        try:
            return Resource.objects.get(id=id)
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, id):
        resource = self.get_resource(id)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        resource = self.get_resource(id)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        _id = id
        resource = self.get_resource(id)
        resource.delete()
        return Response(_id, status=status.HTTP_204_NO_CONTENT)


        