# Generated by Django 2.1.1 on 2019-08-13 02:12

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名称', max_length=20, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, help_text='上级行政区划', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='meeting.Area', verbose_name='上级行政区划')),
            ],
            options={
                'verbose_name': '行政区划',
                'verbose_name_plural': '行政区划',
                'db_table': 'tb_areas',
            },
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='会议名称', max_length=100, verbose_name='会议名称')),
                ('image', models.ImageField(help_text='会议图片', upload_to='meeting', verbose_name='会议图片')),
                ('inform', tinymce.models.HTMLField(help_text='会议通知', verbose_name='会议通知')),
                ('information', tinymce.models.HTMLField(help_text='专家信息', verbose_name='专家信息')),
                ('agenda', tinymce.models.HTMLField(help_text='会议议程', verbose_name='会议议程')),
                ('live_meeting', tinymce.models.HTMLField(help_text='会议直播', verbose_name='会议直播')),
                ('notice', tinymce.models.HTMLField(help_text='会议须知', verbose_name='会议须知')),
                ('hotel_traffic', tinymce.models.HTMLField(help_text='酒店交通', verbose_name='酒店交通')),
                ('contact', tinymce.models.HTMLField(help_text='会务联系', verbose_name='会务联系')),
                ('meet_time', models.DateTimeField(default=0, help_text='会议日期', verbose_name='会议日期')),
            ],
            options={
                'verbose_name': '会议',
                'verbose_name_plural': '会议',
                'db_table': 'meet',
            },
        ),
        migrations.CreateModel(
            name='MeetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='手机号', max_length=11, verbose_name='手机号')),
                ('unit', models.CharField(help_text='单位', max_length=32, verbose_name='单位')),
                ('office', models.CharField(help_text='科室', max_length=32, verbose_name='科室')),
                ('position', models.CharField(help_text='职称', max_length=32, verbose_name='职称')),
                ('id_number', models.CharField(help_text='身份证号', max_length=32, verbose_name='身份证号')),
                ('email', models.EmailField(help_text='邮箱', max_length=254, verbose_name='邮箱')),
                ('is_stay', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=0, help_text='是否住宿', verbose_name='是否住宿')),
                ('stay_requirement', models.SmallIntegerField(choices=[(0, '否'), (1, '是')], default=-1, help_text='住宿要求', verbose_name='住宿要求')),
                ('sex', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, help_text='性别', verbose_name='性别')),
                ('go_time', models.DateField(default=0, help_text='往日期', verbose_name='往日期')),
                ('back_time', models.DateField(default=0, help_text='返日期', verbose_name='返日期')),
                ('city', models.ForeignKey(blank=True, help_text='市', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_addresses', to='meeting.Area', verbose_name='市')),
                ('district', models.ForeignKey(blank=True, help_text='区', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_addresses', to='meeting.Area', verbose_name='区')),
                ('meeting', models.ForeignKey(blank=True, help_text='会议', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record_meet', to='meeting.Meet', verbose_name='会议')),
                ('province', models.ForeignKey(blank=True, help_text='省', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='province_addresses', to='meeting.Area', verbose_name='省')),
            ],
            options={
                'verbose_name': '会议注册',
                'verbose_name_plural': '会议注册',
                'db_table': 'meet_record',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='用户', max_length=32, verbose_name='用户')),
                ('phone', models.CharField(help_text='手机号', max_length=11, verbose_name='手机号')),
                ('meeting', models.ForeignKey(blank=True, help_text='会议', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_meet', to='meeting.Meet', verbose_name='会议')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='meetrecord',
            name='user',
            field=models.ForeignKey(blank=True, help_text='用户', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record_user', to='meeting.User', verbose_name='用户'),
        ),
    ]
