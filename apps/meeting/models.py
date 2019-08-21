from django.db import models

# Create your models here.
from tinymce.models import HTMLField




class Meet(models.Model):
    '''会议'''

    name=models.CharField(max_length=100,verbose_name='会议名称',help_text='会议名称')
    image=models.ImageField(upload_to='meeting',verbose_name='会议图片',help_text='会议图片')
    inform = HTMLField(verbose_name='会议通知',help_text='会议通知')
    information = HTMLField(verbose_name='专家信息',help_text='专家信息')
    agenda = HTMLField(verbose_name='会议议程',help_text='会议议程')
    live_meeting = HTMLField(verbose_name='会议直播',help_text='会议直播')
    notice = HTMLField(verbose_name='会议须知',help_text='会议须知')
    hotel_traffic = HTMLField(verbose_name='酒店交通',help_text='酒店交通')
    contact = HTMLField(verbose_name='会务联系',help_text='会务联系')
    meet_time = models.DateTimeField(default=0, verbose_name='会议日期', help_text='会议日期')
    sign_start_time = models.DateTimeField(verbose_name='签到开始时间', help_text='签到开始时间',null=True,blank=True)
    sign_end_time = models.DateTimeField(verbose_name='签到结束时间', help_text='签到结束时间',null=True,blank=True)



    class Meta:
        db_table = 'meet'
        verbose_name = '会议'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class User(models.Model):
    '''用户'''
    username=models.CharField(max_length=32,verbose_name='用户',help_text='用户')
    phone=models.CharField(max_length=11,verbose_name='手机号',help_text='手机号')
    meeting=models.ForeignKey(Meet,related_name='user_meet',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='会议',help_text='会议')



    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



class MeetRecord(models.Model):
    '''会议注册'''

    stay_choice = (
        (0, '否'),
        (1, '是')
    )
    stay_requirement_choice = (
        (0, '单间'),
        (1, '标间'),
        (2, '包房')
    )

    sex_type = (
        (0, '男'),
        (1, '女')
    )

    sign_choice = (
        (0, '未签到'),
        (1, '已签到'),
        (2,'超时未签到')
    )

    meeting=models.ForeignKey(Meet,related_name='record_meet',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='会议',help_text='会议')
    user=models.ForeignKey(User,related_name='record_user',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='用户',help_text='用户')
    phone = models.CharField(max_length=11, verbose_name='手机号',help_text='手机号')
    province = models.ForeignKey('Area', on_delete=models.SET_NULL,null=True,blank=True, related_name='province_addresses', verbose_name='省',help_text='省')
    city = models.ForeignKey('Area', on_delete=models.SET_NULL,null=True,blank=True, related_name='city_addresses', verbose_name='市', help_text='市')
    district = models.ForeignKey('Area', on_delete=models.SET_NULL,null=True,blank=True, related_name='district_addresses', verbose_name='区',help_text='区')
    unit=models.CharField(max_length=32,verbose_name='单位',help_text='单位')
    office=models.CharField(max_length=32,verbose_name='科室',help_text='科室')
    position=models.CharField(max_length=32,verbose_name='职称',help_text='职称')
    id_number=models.CharField(max_length=32,verbose_name='身份证号',help_text='身份证号')
    email=models.EmailField(verbose_name='邮箱',help_text='邮箱')
    is_stay=models.SmallIntegerField(default=0, choices=stay_choice, verbose_name='是否住宿', help_text='是否住宿')
    stay_requirement=models.SmallIntegerField(default=-1, choices=stay_choice, verbose_name='住宿要求', help_text='住宿要求')
    sign_in=models.SmallIntegerField(default=0, choices=sign_choice, verbose_name='签到状态', help_text='签到状态')
    sex = models.SmallIntegerField(default=0, choices=sex_type, verbose_name='性别',help_text='性别')
    go_time=models.DateField(default=0,verbose_name='往日期',help_text='往日期')
    back_time=models.DateField(default=0,verbose_name='返日期',help_text='返日期')



    class Meta:
        db_table = 'meet_record'
        verbose_name = '会议注册'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username




class Area(models.Model):
    """
    行政区划
    """
    name = models.CharField(max_length=20, verbose_name='名称',help_text='名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True, verbose_name='上级行政区划',help_text='上级行政区划')

    class Meta:
        db_table = 'tb_areas'
        verbose_name = '行政区划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


