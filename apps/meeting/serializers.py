from rest_framework import serializers

from meeting.models import User, Area, MeetRecord, Meet


class GetMeetInfoSerializer(serializers.ModelSerializer):
    """获取注册会议信息"""
    meeting_id=serializers.IntegerField(source='meeting.id')
    name=serializers.CharField(source='meeting.name')
    class Meta:
        model = User
        fields = ('id', 'username','phone','meeting_id','name')



class AreaSerializer(serializers.ModelSerializer):
    """
    行政区划信息序列化器
    """
    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaSerializer(serializers.ModelSerializer):
    """
    子行政区划信息序列化器
    """
    subs = AreaSerializer(many=True, read_only=True)
    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')


class SubAreaSerializer2(serializers.ModelSerializer):
    """
    子行政区划信息序列化器
    """
    subs = SubAreaSerializer(many=True, read_only=True)
    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')



class MeetRegisterSerializer(serializers.ModelSerializer):
    '''会议注册'''

    class Meta:
        model = MeetRecord
        fields = '__all__'






class MeetRegisterSerializer2(serializers.Serializer):
    """
    会议注册
    """
    user_id = serializers.IntegerField()
    meeting_id = serializers.IntegerField()

    def validate(self, attrs):

        user = User.objects.filter(id=attrs['user_id'], meeting_id=attrs['meeting_id'])
        if not user:
            raise serializers.ValidationError('用户不存在')

        return attrs




class IndexImageSerializer(serializers.ModelSerializer):
    '''会议首页图片'''

    class Meta:
        model = Meet
        fields = ('image',)







class MeetAdminSerializer(serializers.ModelSerializer):
    '''会议后台'''
    meet_time = serializers.DateTimeField(format="%Y-%m-%d")
    sign_start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    sign_end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Meet
        fields = '__all__'




class MeetRegisterAdminSerializer(serializers.ModelSerializer):
    '''会议注册后台'''

    class Meta:
        model = MeetRecord
        fields = '__all__'



class MeetRegisterAdminSerializer2(serializers.ModelSerializer):
    '''会议注册后台'''

    class Meta:
        model = MeetRecord
        fields = '__all__'
        depth=1