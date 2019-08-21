from django.shortcuts import render

from rest_framework import mixins, status, viewsets, filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from meeting.models import MeetRecord, User, Area, Meet
from meeting.serializers import GetMeetInfoSerializer, SubAreaSerializer2, MeetRegisterSerializer, IndexImageSerializer, \
    MeetAdminSerializer, MeetRegisterAdminSerializer, MeetRegisterAdminSerializer2, MeetRegisterSerializer2
from utils.paginator import GoodsPagination


class MeetRegisterView(viewsets.ModelViewSet):
    '''会议注册'''

    queryset = MeetRecord.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return MeetRegisterSerializer
        else:
            return MeetRegisterSerializer2


    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        dict = {}
        user=User.objects.get(id=request.query_params['user_id'],meeting_id=request.query_params['meeting_id'])
        ser=GetMeetInfoSerializer(instance=user,many=False)
        dict['user_info']=ser.data
        sex_type = MeetRecord.sex_type
        stay_choice = MeetRecord.stay_choice
        stay_requirement_choice = MeetRecord.stay_requirement_choice
        dict['sex']=sex_type
        dict['is_stay']=stay_choice
        dict['stay_requirement']=stay_requirement_choice
        return Response(dict)




class AreasViewSet(CacheResponseMixin,ReadOnlyModelViewSet):
    """
    行政区划信息
    """
    serializer_class = SubAreaSerializer2
    queryset = Area.objects.filter(parent_id=None)



class IndexImageView(mixins.RetrieveModelMixin,GenericViewSet):
    '''会议首页图片'''

    queryset = Meet.objects.all()
    serializer_class = IndexImageSerializer




class MeetInformView(RetrieveAPIView):
    '''会议相关信息'''

    queryset = Meet.objects.all()
    serializer_class = MeetAdminSerializer





# 后台管理页面
class MeetAdminView(viewsets.ModelViewSet):
    '''会议后台'''
    serializer_class = MeetAdminSerializer
    queryset = Meet.objects.all()
    pagination_class = GoodsPagination  # 指定自定义分页类
    permission_classes = [IsAdminUser, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)





class MeetRegisterAdminView(viewsets.ModelViewSet):
    '''会议注册后台'''

    queryset = MeetRecord.objects.all()
    pagination_class = GoodsPagination  # 指定自定义分页类
    permission_classes = [IsAdminUser, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username','meeting__name')


    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return MeetRegisterAdminSerializer
        else:
            return MeetRegisterAdminSerializer2





