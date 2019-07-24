from django.contrib import admin
from .models import Product, Mobile, Student
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'prize', 'pub_date', 'image')
    list_filter = ('title', 'prize', 'pub_date')
    search_fields = ('title',)



admin.site.register(Product, ProductAdmin)

class MobileAdmin(admin.ModelAdmin):
    list_display = ('name', 'prize1')
    list_filter = ('name', 'prize1' )
    search_fields = ('name',)

admin.site.register(Mobile, MobileAdmin)



class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'language', 'grades', 'gender')
    list_filter = ('language', 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'products/change_list_graph.html'


admin.site.register(Student, StudentAdmin)
