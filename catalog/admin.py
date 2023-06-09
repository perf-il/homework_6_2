from django.contrib import admin

from catalog.models import Product, Category, Blog, ProductVersion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created_by', 'is_public',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name', 'slug', 'content', 'data_creating', 'is_published', 'view_count',)
    prepopulated_fields = {'slug': ('title_name',)}


@admin.register(ProductVersion)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active',)


