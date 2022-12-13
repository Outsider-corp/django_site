from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Categories
from .utils import FirstMixin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(FirstMixin, admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ["id", "title", "category", "created_time", "is_publ", "get_image"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "content"]
    list_editable = ["is_publ"]
    list_filter = ["is_publ", "category"]
    fields = ["category", "title", "content", "is_publ", "get_image", 'image', 'views', "created_time"]
    readonly_fields = ["created_time", "get_image", 'views']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=75>')

    get_image.short_description = "Image"


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    ordering = ["id"]


admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategoriesAdmin)

admin.site.site_title = "Admin Panel"
admin.site.site_header = FirstMixin.text_mix
