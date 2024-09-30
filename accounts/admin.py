from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # 表示するフィールドのセットアップ
    list_display = ('email', 'name', 'get_review_average', 'review_count', 'is_staff', 'is_active', 'created_at')
    list_filter = ('is_staff', 'is_active', 'sex')
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'age', 'sex', 'contact_address', 'bio', 'review_count', 'review_sum')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at')}),
        (_('Matching info'), {'fields': ('cur_matching', 'matching_history', 'wait', 'done', 'semi_comp')}),
    )

    readonly_fields = ('created_at', 'updated_at')  # 'created_at'と'updated_at'を読み取り専用に設定

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'age', 'sex', 'contact_address', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    filter_horizontal = ('matching_history',)

    def get_review_average(self, obj):
        return obj.review_average
    get_review_average.short_description = 'Review Average'  # カラムヘッダーの名前

admin.site.register(User, UserAdmin)