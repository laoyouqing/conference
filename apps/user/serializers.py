import re

from rest_framework import serializers

from meeting.models import User, Meet


class LoginSerializer(serializers.ModelSerializer):
    """登录"""
    phone = serializers.CharField(min_length=11,max_length=11,error_messages={'min_length': '仅允许11个字符的手机号','max_length': '仅允许11个字符的手机号'})

    def validate_phone(self, value):
        """验证手机号"""
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value


    def create(self, validated_data):
        """创建用户"""
        user=User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id','username','phone','meeting')



class AllMeetSerializer(serializers.ModelSerializer):
    """获取所有会议"""

    class Meta:
        model = Meet
        fields = ('id', 'name')










# 后台管理序列化

class UserSerializer(serializers.ModelSerializer):
    '''用户'''
    class Meta:
        model = User
        fields = '__all__'
