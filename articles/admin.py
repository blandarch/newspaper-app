from django.contrib import admin
from .models import Article, Comment
#from django.contrib.admin import TabularInLine

class CommentInLine(admin.TabularInline):
    model = Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)