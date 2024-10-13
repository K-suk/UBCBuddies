from django.contrib import admin
from .models import FemaleDatingQueue, FemaleDrinkQueue, FemaleGymQueue, MaleDatingQueue, MaleDrinkQueue, MaleGymQueue, MaleQueue, FemaleQueue

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
    
class MaleGymQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class FemaleGymQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class MaleDrinkQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class FemaleDrinkQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class MaleDatingQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

class FemaleDatingQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count')
    filter_horizontal = ('users',)

    def user_count(self, obj):
        return obj.users.count()
    user_count.short_description = 'User Count'

admin.site.register(MaleQueue, MaleQueueAdmin)
admin.site.register(FemaleQueue, FemaleQueueAdmin)
admin.site.register(MaleGymQueue, MaleGymQueueAdmin)
admin.site.register(FemaleGymQueue, FemaleGymQueueAdmin)
admin.site.register(MaleDrinkQueue, MaleDrinkQueueAdmin)
admin.site.register(FemaleDrinkQueue, FemaleDrinkQueueAdmin)
admin.site.register(MaleDatingQueue, MaleDatingQueueAdmin)
admin.site.register(FemaleDatingQueue, FemaleDatingQueueAdmin)