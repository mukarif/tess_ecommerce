from django.contrib import admin
from web.models import Profile

# Register your models here.


@admin.register(Profile, site=admin.site)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'nama_toko',
                    'alamat', 'phone', 'is_penjual', 'is_admin')
    search_fields = ('user__id', 'user__first_name', 'user__last_name',
                     'nama_toko', 'phone')
    # inlines = [
    #     JabatanInline,
    # ]

    def first_name(self, obj):
        if obj.user:
            return obj.user.first_name
        else:
            return ""
