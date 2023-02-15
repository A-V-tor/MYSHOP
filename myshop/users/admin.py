from django.contrib import admin
from .models import User


<<<<<<< HEAD
admin.site.register(User)
=======
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
    )
    list_filter = ('username',)


admin.site.register(User, UserAdmin)
>>>>>>> 6f3665d (add: приложение users)
