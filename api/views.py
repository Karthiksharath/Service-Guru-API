from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializer,WorkSerializer

from api.models import Customer,Work


class CustomerViewSetView(ModelViewSet):

    serializer_class = CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        
        serializer.save(technician=self.request.user)



    @action(methods=['post'],detail=True)   # if id in url then detil=True else detail=False
    def add_work(self,request,*args,**kwargs):

        # customer_instance = self.get_object()

        id = kwargs.get("pk")

        customer_instance =  Customer.objects.get(id=id)

        serializer = WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_instance)

            return Response(data=serializer.data)

        else:

            return Response(data=serializer.errors)


"""

rest framework--->generics.py

    1-class CreateApiView
    2-class ListApiView
    3-class RetrieveApiView
    4-class UpdateApiView
    5-class DestroyApiView



class Workadd(CreateAPiView)

    serializer_class = Workserializer

    def perform_create(self,serializer):
        id = kwargs.get("pk")
        customer_instance = customer.objwcts.get(id=id)
        serializer.save(customer=customer_instance)

"""


class WorkMixinView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    queryset = Work.objects.all()

    serializer_class = WorkSerializer





        




