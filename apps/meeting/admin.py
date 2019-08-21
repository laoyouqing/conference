from django.contrib import admin

# Register your models here.
from meeting.models import Area, Meet, User, MeetRecord

admin.site.register(Area)
admin.site.register(Meet)
admin.site.register(User)
admin.site.register(MeetRecord)