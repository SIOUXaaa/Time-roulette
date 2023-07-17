import os

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
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
    avatar = serializers.ImageField(max_length=255, required=False, source='avatar.url')

    def create(self, validated_data):
        password = validated_data.pop('password')
        avatar = validated_data.pop('avatar', None)
        user = User(**validated_data)
        user.password = password
        if avatar:
            user.avatar = avatar
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.name
        instance.password = validated_data.name
        # instance.avatar = validated_data.avatar

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


# {
#      username,
#      password
# }
@api_view(['POST'])
def login(req):
    username = req.data.get('username')
    password = req.data.get('password')
    try:
        user = User.objects.get(name=username)
        password_match = check_password(password, user.password)
        if password_match:
            if user.avatar:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'login_success': True,
                    'avatar': user.avatar.url
                }
            else:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'login_success': True,
                }
        else:
            data = {
                'msg': '密码错误',
                'login_success': False
            }
        return Response(data)
    except User.DoesNotExist:
        return Response('用户不存在')


# {
#     name
#     password
# }
@api_view(['POST'])
def register(req):
    if User.objects.filter(name=req.data.get('name')).exists():
        return Response({'msg': '用户名已存在'}, status=400)
    serializer = UserSerializers(data=req.data)
    if serializer.is_valid():
        serializer.validated_data['password'] = make_password(req.data['password'])
        serializer.save()
        return Response({'msg': '注册成功'}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def upload_avatar(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
        avatar = req.FILES.get('file')
        if user.avatar:
            old_avatar = os.path.join(settings.MEDIA_ROOT, f'avatar/{user.avatar}')
            if default_storage.exists(old_avatar):
                default_storage.delete(old_avatar)
        file_ext = os.path.splitext(avatar.name)[1]
        file_path = f'avatar/{user_id}_avatar' + file_ext
        file_path = default_storage.save(file_path,
                                         ContentFile(avatar.read()))
        user.avatar = file_path
        user.save()
        serializer = UserSerializers(data=user)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
    except User.DoesNotExist:
        return Response(status=404)
    return Response({'success': True, 'file_path': file_path})


@api_view(['GET'])
def get_avatar(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
        data = {
            'avatar': user.avatar.url
        }
        return Response(data)
    except User.DoesNotExist:
        return Response(status=404)


# {
#     "username": "test11"
# }
@api_view(['PUT'])
def update_username(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'msg': '用户不存在'}, status=404)
    username = req.data.get('username')
    if username and User.objects.filter(name=username).exclude(id=user_id).exists():
        return Response({'msg': '用户名已存在'}, status=400)
    if username:
        user.name = username
        user.save()
    return Response({'msg': '提交成功'}, status=200)


# {
#     "password"
#     "newPassword"
# }
@api_view(['PUT'])
def update_password(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'msg': '用户不存在'}, status=404)
    password = req.data.get('password')
    new_password = req.data.get('newPassword')
    if check_password(password, user.password):
        user.password = make_password(new_password)
        user.save()
    else:
        return Response({'msg': '密码错误'}, status=400)
    return Response({'msg': '更改密码成功'}, status=200)


@api_view(['GET'])
def get_schedule(req, user_id):
    schedules = Schedule.objects.filter(user=user_id)
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
