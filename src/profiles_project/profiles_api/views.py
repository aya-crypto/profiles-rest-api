from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ Retuens a list APIVIEW Features """
        an_apiview=[
             "Uses HTTP method as function (get,post,patch,put,delete)",
             "It is similar to a traditional Django View ",
             "Gives you the most control over your logic",
             "It managed manually to URLs"
        ]
        return Response({"message":"Hello","an_apiview":an_apiview})

    def post(self,request):
        """create a hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request , pk=None):
        """handels updatong an object"""

        return Response({'method':'put'})


    def patch(self, request , pk=None):
        """ Patch request , only update fields provided in request"""

        return Response({'method':'patch'})

    def delete(self, request,pk=None):
        """delete an object"""

        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """ test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return hello message"""
        a_viewset=[
            'Uses actions (list,create,retrieve ,update ,partial update)',
            'Automatically maps URLS using Routers',
            "Provides more functionality with less code",
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self,request):
        """create a new hello message """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retreive(self,request, pk=None):
        """handels getting an object by its id """

        return Response({'http_method':'GET'})

    def update(self,request, pk=None):
        """handels updating an object  """

        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk=None):
        """handels updating part of an object"""

        return Response({'http_method':'PATCH'})

    def destory(self, request,pk=None):
        """handels removing an object"""

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handels creating and updating profiles ."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #permissions
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
