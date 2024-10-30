from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel
# Create your models here.


User = get_user_model()


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Location(PublishedModel):
    name = models.CharField(max_length=256)


class Post(PublishedModel):
    title = models.CharField('Название', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('-pub_date',)
