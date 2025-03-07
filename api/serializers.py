
from rest_framework import serializers

from api.models import Customer,Work


class WorkSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField(read_only=True)  # to get customer name instead of id in add work serializer

    class Meta:

        model = Work

        fields = "__all__"

        read_only_fields = ["id","customer","created_date","updated_date","is_active"]



class CustomerSerializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    work_count = serializers.CharField(read_only=True)

    work_total = serializers.CharField(read_only=True)

    works = WorkSerializer(many=True,read_only=True)


    class Meta:

        model=Customer

        fields="__all__"

        read_only_fields=["id","technician","status","created_date","update_date","is_active"]