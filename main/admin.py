from django.contrib import admin
from .models import *
admin.site.register(Talaba)
admin.site.register(Kitob)

@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism')
    list_filter = ('id',)
    search_fields = ('ism',)

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism')
    list_filter = ('id',)
    search_fields = ('ism',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'olingan_sana', 'qaytarish_sana', 'talaba', 'kutubxonachi')
    list_filter = ('qaytarish_sana',)