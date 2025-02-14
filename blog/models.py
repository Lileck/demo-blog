from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')
        class Like(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='публикация',
        on_delete=models.CASCADE,
        related_name='likes' 
    )
    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    reaction = models.SmallIntegerField(
        verbose_name='реакция',
        choices=((1, 'Like'), (-1, 'Dislike')),  
        default=1
    )

    user = models.ForeignKey( # Add User model here
        settings.AUTH_USER_MODEL,
        verbose_name = "пользователь",
        on_delete = models.CASCADE
    )

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        unique_together = ('post', 'user')  

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='публикация',
        on_delete=models.CASCADE,
        related_name='comments'  
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=255
    )
    comment = models.TextField(
        verbose_name='комментарий'
    )
    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    parent_comment = models.ForeignKey(
        'self', 
        verbose_name='родительский комментарий',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='replies'
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

class Donat(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255
    )
    link = models.URLField(
        verbose_name='ссылка'
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
        upload_to='donations/' 
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пожертвование'
        verbose_name_plural = 'пожертвования'
