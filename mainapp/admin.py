from django.contrib import admin

from .models import ImageModel


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_display_links = ['id', 'image']

    class Meta:
        model = ImageModel


admin.site.register(ImageModel, ImageModelAdmin)
