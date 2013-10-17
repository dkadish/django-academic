from django.contrib import admin
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import *
from academic.settings import *

class InvolvementInline(admin.TabularInline):
    verbose_name = 'Involvement'
    verbose_name_plural = 'Involvements'
    model = Involvement
    extra = 5
    
class ProjectAdmin(admin.ModelAdmin):
    inlines = (InvolvementInline,)
    prepopulated_fields = {
	'slug': ('short_title',)
    }
    fieldsets = (
        (None, {
                'fields': (
                    'short_title',
                    'slug',
                    'title',
                    'start_year',
                    'end_year',
                    'presented_year',
                    'excerpt',
                    'topic',
                    'description',
                    'publications',
                    'image',
                    'image_caption'),}),
        (_('Extra information'), {
                'classes': (
                    'collapse closed collapse-closed',),
                'fields': (
                    'related_topics',
                    'redirect_to',
                    'downloads',
                    'organizations',
                    'sponsors',
                    'footer'),})
        )
    filter_horizontal = [
        'downloads',
        'related_topics',
        'organizations',
        'sponsors',
        'publications']
    list_display_links = [
        'title']
    list_display = [
        'title',
        'short_title',
        'excerpt',
        'topic']
admin.site.register(Project, ProjectAdmin)

class TopicAdmin(admin.ModelAdmin):
#     class Media:
#         js = (
#             TINYMCE_MCE_JS,
#             TINYMCE_SETUP_JS, )
    prepopulated_fields = {
	'slug': ('title',)
    }
    list_display_links = [
        'title']
    list_display = [
        'title',
        'highlight',
        'highlight_order',
        'description']
admin.site.register(Topic, TopicAdmin)

class RoleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Role, RoleAdmin)

class InvolvementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Involvement, InvolvementAdmin)