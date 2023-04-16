from django.contrib import admin
from communication.models import ImageFeedback, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'theme',
        'datetime',
        'status',
        'text',
    )
    list_editable = ('status',)
    list_filter = ('datetime', 'theme', 'status')


class ImageFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'feedback',
        'image',
    )
    list_filter = ('feedback',)


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ImageFeedback, ImageFeedbackAdmin)
