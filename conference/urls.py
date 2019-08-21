"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from conference.settings import MEDIA_ROOT
from meeting.views import MeetRegisterView, AreasViewSet, IndexImageView, MeetAdminView, MeetRegisterAdminView, \
    MeetInformView
from user.views import AllMeetView, LoginView, UserAdminView

router = DefaultRouter()
router.register('areas', AreasViewSet, base_name='areas')
router.register('image', IndexImageView, base_name='image')
router.register('user_admin', UserAdminView, base_name='user_admin')
router.register('meet_admin', MeetAdminView, base_name='meet_admin')
router.register('meet_register_admin', MeetRegisterAdminView, base_name='meet_register_admin')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path("api-docs/", include_docs_urls("API文档")),
    path('', include(router.urls)),
    path('admin_login/', obtain_jwt_token),

    path('all_meet/', AllMeetView.as_view({'get':'list'})),
    path('login/', LoginView.as_view({'post':'create'})),
    path('meet_info/', MeetRegisterView.as_view({'get':'list','post':'create'})),
    path('meet/<int:pk>/', MeetInformView.as_view()),

]
