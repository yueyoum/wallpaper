from django.contrib import admin

from main.models import Phone, WallPaper

@admin.register(Phone)
class AdminPhone(admin.ModelAdmin):
    list_display = (
            'id', 'tp', 'app_id',
            'first_login', 'last_login',
            )

    list_filter = ('app_id',)

