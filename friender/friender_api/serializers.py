from rest_framework import serializers
from appointment.models import *


class EstablishmentsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # category = serializers.CharField(max_length=200)
    # address = serializers.CharField(max_length=200)
    # phone = serializers.CharField(max_length=200)

    class Meta:
        model = Establishments
        fields = ('name', 'category', 'address', 'phone')

    def create(self, validated_data):
        return Establishments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ('name_hobby', 'category')

    def create(self, validated_data):
        return Hobbies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_hobby = validated_data.get('name_hobby', instance.name_hobby)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
