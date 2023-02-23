from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание группы')

    class Meta:
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:16]


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        default_related_name = 'posts'

    def __str__(self):
        return self.text[32]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Комментарий',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        on_delete=models.CASCADE,
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True)

    class Meta:
        default_related_name = 'comments'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[32]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        verbose_name='Подписка',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following',),
                name='follow_unique'
            ),
            models.CheckConstraint(
                check=~Q(user=F('following')),
                name='not_following'
            ),
        ]
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user.username} >> {self.following.username}'
