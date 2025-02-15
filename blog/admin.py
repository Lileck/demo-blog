from django.contrib import admin

from .models import Post

@admin.register(Post)  # Альтернативный способ регистрации модели
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'лаки', 'комментарии', 'донаты')  # Поля для отображения в списке
    fields = ('title', 'content', 'picture', 'slug', 'category', 'лаки', 'комментарии', 'донаты')  # Поля для отображения в форме редактирования

