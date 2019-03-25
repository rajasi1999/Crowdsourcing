from django.contrib import admin
from .models import User,Fundraiser,Donor
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(UserAdmin):
    form = UserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "is_fundraiser",
                    "is_donor",
                    "aadhar_id",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)

admin.site.register(Fundraiser)
admin.site.register(Donor)
