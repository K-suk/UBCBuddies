from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=150,
        null=True,
        blank=False
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    contact_address = models.CharField(
        verbose_name=("contact_address"),
        max_length=150,
        null=True,
        blank=True
    )
    cur_matching = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='current_match')  # 現在のマッチ
    matching_history = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=1024)
    profile_image = models.URLField(max_length=255, null=True, blank=True) 
    wait = models.BooleanField(default=False)  # 待機中かどうかを示すフラグ
    done = models.BooleanField(default=True)  # マッチングが完了したかどうかを示すフラグ
    review_count = models.PositiveIntegerField(default=0)  # レビュー数
    review_sum = models.PositiveIntegerField(default=0)    # レビューの合計点
    semi_comp = models.BooleanField(default=False)

    @property
    def review_average(self):
        if self.review_count > 0:
            return self.review_sum / self.review_count
        return 0.0

    def add_review(self, rating):
        self.review_count += 1
        self.review_sum += rating
        self.save()

    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # スーパーユーザー作成時にemailも設定する

    def __str__(self):
        return self.email