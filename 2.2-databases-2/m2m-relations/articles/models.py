from django.db import models


from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Тэг')
    articles = models.ManyToManyField('Article', through='Relationship',
                                      related_name='tags')

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-is_main', 'tag']
