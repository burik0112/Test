from django.contrib import admin

from user.models import TimeSheet


# Register your models here.

@admin.register(TimeSheet)
class TimeSheetModelAdmin(admin.ModelAdmin):
    list_display = ['Working', 'TimeSheetCodeEN', 'TimeSheetCodeRU', 'TimeSheetCodeTR', 'TimeSheetCode', 'DescriptionRU']
