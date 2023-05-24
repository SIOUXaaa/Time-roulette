from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import *


# Create your views here.

class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)  # Field renamed because it was a Python reserved word.
    avatar = serializers.ImageField(max_length=255, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        avatar = validated_data.pop('avatar', None)
        user = User(**validated_data)
        user.password = password
        if avatar:
            user.avatar = avatar
        user.save()
        return user


class ScheduleSerializers(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.contents = validated_data.get('contents', instance.contents)
        instance.address = validated_data.get('address', instance.address)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

    class Meta:
        model = Memo
        fields = ['schedule_id', 'user', 'title', 'contents', 'address', 'time']


class Memo(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def update(self, instance, validated_data):
        instance.contents = validated_data.get('contents', instance.contents)
        instance.done = validated_data.get('done', instance.done)
        instance.reminded = validated_data.get('reminded', instance.reminded)
        instance.reminded = validated_data.get('reminded', instance.reminded)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

    class Meta:
        model = Memo
        fields = ['memo_id', 'user', 'contents', 'contents', 'done', 'reminded', 'time']


class UserView(APIView):
    def get(self, req, pk):
        user_list = User.objects.filter(pk=pk)
        serializer = UserSerializers(instance=user_list, many=True)
        return Response(serializer.data)

    def post(self, req):
        username = req.data.get('username')
        password = req.data.get('password')
        serializer = UserSerializers(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['POST'])
def login(req):
    username = req.data.get('username')
    password = req.data.get('password')
    try:
        user = User.objects.get(name=username)
        serializer = UserSerializers(instance=user, many=False)
        if user.password == password:
            return Response(serializer.data)
        else:
            return Response({'msg': "该用户不存在"})
    except User.DoesNotExist:
        return Response('用户不存在')


@api_view(['POST'])
def register(req):
    serializer = UserSerializers(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_schedule(req):
    schedules = Memo.objects.all()
    # print(schedules.values())
    serializer = ScheduleSerializers(schedules, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_schedule(req, schedule_id):
    try:
        schedule = Schedule.objects.get(pk=schedule_id)
    except Schedule.DoesNotExist:
        return Response(status=404)

    serializer = ScheduleSerializers(schedule, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_memo(req):
    memos = Memo.objects.all()
    # print(memos.values())
    serializer = ScheduleSerializers(memos, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_memo(req, memo_id):
    try:
        memo = Memo.objects.get(pk=memo_id)
    except Memo.DoesNotExist:
        return Response(status=404)

    serializer = ScheduleSerializers(memo, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
