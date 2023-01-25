from django.contrib import admin
from .models import LogRecord


class LogRecordAdmin(admin.ModelAdmin):
    list_display = ("pk", "comment", "date_created", "user")


admin.site.register(LogRecord, LogRecordAdmin)

# Register your models here.
