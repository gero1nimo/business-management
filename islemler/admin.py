from django.contrib import admin
from .models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.    

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('islem_id', 'islem_tarihi', 'islem_turu', 'islem_miktari', 'yapan_kisi', 'aciklama')
    search_fields = ('aciklama', 'yapan_kisi')
    list_filter = ('islem_turu', 'islem_tarihi')


admin.site.register(Transaction, TransactionAdmin)
