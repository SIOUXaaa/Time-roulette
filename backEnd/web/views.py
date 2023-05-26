from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import *


# Create your views here.

class UserSerializers(serializers.ModelSerializer):
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

    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'avatar']


class ScheduleSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.contents = validated_data.get('contents', instance.contents)
        instance.address = validated_data.get('address', instance.address)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'user', 'title', 'contents', 'address', 'time']


class MemoSerializers(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def update(self, instance, validated_data):
        instance.contents = validated_data.get('contents', instance.contents)
        instance.done = validated_data.get('done', instance.done)
        instance.reminded = validated_data.get('reminded', instance.reminded)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

    class Meta:
        model = Memo
        fields = ['memo_id', 'user', 'contents', 'done', 'reminded', 'time']


@api_view(['POST'])
def login(req):
    username = req.data.get('username')
    password = req.data.get('password')
    try:
        user = User.objects.get(name=username)
        # serializer = UserSerializers(instance=user, many=False)
        if user.password == password:
            data = {
                'id': user.id,
                'name': user.name,
                # 'avatar': user.avatar,
                'login_success': True
            }
        else:
            data = {
                'msg': '密码错误',
                'login_success': False
            }
        return Response(data)
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
def get_schedule(req, user_id):
    schedules = Schedule.objects.filter(user=user_id)
    # print(schedules.values())
    serializer = ScheduleSerializers(schedules, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_schedule(req, schedule_id):
    try:
        schedule = Schedule.objects.get(pk=schedule_id)
    except Schedule.DoesNotExist:
        return Response({'msg': 'not found'}, status=404)

    serializer = ScheduleSerializers(schedule, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def add_schedule(req):
    serializer = ScheduleSerializers(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_schedule(req, schedule_id):
    try:
        schedule = Schedule.objects.get(pk=schedule_id)
        schedule.delete()
        return Response({"msg": "删除成功"})
    except Schedule.DoesNotExist:
        return Response(status=404)


@api_view(['DELETE'])
def delete_all_schedule(req, user_id):
    try:
        schedules = Schedule.objects.filter(user=user_id)
        schedules.delete()
        return Response({"msg": "删除成功"}, status=204)
    except Schedule.DoesNotExist:
        return Response(status=404)


@api_view(['GET'])
def get_memo(req, user_id):
    memos = Memo.objects.filter(user=user_id, done=False)
    # print(memos.values())
    serializer = MemoSerializers(memos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_memo_done(req, user_id):
    memos = Memo.objects.filter(user=user_id, done=True)
    serializer = MemoSerializers(memos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_memo(req):
    serializer = MemoSerializers(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response(serializer.errors)


@api_view(['PUT'])
def update_memo(req, memo_id):
    try:
        memo = Memo.objects.get(pk=memo_id)
    except Memo.DoesNotExist:
        return Response({'msg': 'not found'}, status=404)

    serializer = MemoSerializers(memo, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_memo(req, memo_id):
    try:
        memo = Memo.objects.get(pk=memo_id)
        memo.delete()
        return Response({"msg": "删除成功"})
    except Memo.DoesNotExist:
        return Response(status=404)


@api_view(['PUT'])
def delete_all_memo(req, user_id):
    try:
        memos = Memo.objects.filter(user=user_id)
        for memo in memos:
            memo.done = True
            memo.save()
        serializer = MemoSerializers(data=memos, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response({"msg": "清除代办成功"}, status=204)
    except Memo.DoesNotExist:
        return Response(status=404)
