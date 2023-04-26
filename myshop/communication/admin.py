from django.contrib import admin

from django.contrib import messages
from communication.models import ImageFeedback, Feedback, Info
from .forms import FeedbackAdminForm, InfoAdminForm


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
    form = FeedbackAdminForm


class ImageFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'feedback',
        'image',
    )
    list_filter = ('feedback',)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    form = InfoAdminForm

    def has_change_permission(self, request, obj=0):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change, **kwargs):
        """При попытки создать более 1 записи в Info
        уведомление о невозможности это сделать.
        """
        if not change and Info.objects.exists():
            self.message_user(
                request,
                'Может быть только один экземпляр этой модели.',
                messages.ERROR,
            )
            return None
        super().save_model(request, obj, form, change)


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ImageFeedback, ImageFeedbackAdmin)
admin.site.register(Info, InfoAdmin)
