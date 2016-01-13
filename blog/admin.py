from django.contrib import admin
from blog.models import Article, Comment


# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['title']}),
        (None, {'fields': ['text']}),
        (None, {'fields': ['user']}),
        (None, {'fields': ['image']}),
    ]
    inlines = [CommentInLine]
    list_display = ('title', 'user')
    list_filter = ['title', 'user']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)