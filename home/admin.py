from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","brand","category","image","stock","labels")
    list_filter = ("category","brand","stock","labels")
    search_fields = ("name","desription")

admin.site.register(CustomerReview)
admin.site.register(Cart)