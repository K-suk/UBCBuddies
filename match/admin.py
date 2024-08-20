from django.contrib import admin
from .models import MaleQueue, FemaleQueue

class MaleQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class FemaleQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

admin.site.register(MaleQueue, MaleQueueAdmin)
admin.site.register(FemaleQueue, FemaleQueueAdmin)