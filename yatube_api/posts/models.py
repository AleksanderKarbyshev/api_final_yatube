from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название группы',
        max_length=50
    )
    slug = models.SlugField(
        verbose_name='Слаг группы',
        unique=True
    )
    description = models.TextField(verbose_name='Описание группы')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    text = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('pub_date',)

    def __str__(self):
        return (f'{self.author.username} - {self.pub_date} - '
                f'{self.text}')


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Публикация',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (f'{self.author.username} - {self.created} - '
                f'{self.post.text} - {self.text}')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscriber'
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'following')

    def clean(self):
        if self.user == self.following:
            raise ValidationError(
                'Извините, но подписаться на самого себя нельзя :(')
        if Follow.objects.filter(
                user=self.user,
                following=self.following).exists():
            raise ValidationError('Вы уже подписаны на этого автора.')

    def __str__(self):
        return (f'{self.user} подписан на {self.following}')
