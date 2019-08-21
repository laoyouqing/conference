from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from meeting.models import Meet, User
from user.serializers import AllMeetSerializer, LoginSerializer, UserSerializer
from utils.paginator import GoodsPagination


class AllMeetView(mixins.ListModelMixin,GenericViewSet):
    '''获取所有会议'''
    queryset = Meet.objects.all()
    serializer_class = AllMeetSerializer


class LoginView(mixins.CreateModelMixin,GenericViewSet):
    '''登录'''

    queryset = User.objects.all()
    serializer_class = LoginSerializer



def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


class UserAdminView(viewsets.ModelViewSet):
    '''用户后台'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = GoodsPagination  # 指定自定义分页类
    permission_classes = [IsAdminUser, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','phone')