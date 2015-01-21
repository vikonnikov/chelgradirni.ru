# coding: cp1251

from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    position = models.IntegerField()

    def __unicode__(self):
        return self.title

class Keyword(models.Model):
    class Meta:
        verbose_name = u'ключевое слово'
        verbose_name_plural = u'Ключевые слова'

    phrase = models.CharField(max_length=100)

    def __unicode__(self):
        return self.phrase

class Page(models.Model):
    class Meta:
        verbose_name = u'страницу'
        verbose_name_plural = u'Страницы'

    title = models.CharField(u'Заголовок', max_length=100,)
    url = models.CharField(u'Ссылка', max_length=100)
    content = models.TextField(u'Содержимое')
    description = models.TextField(u'Описание', max_length=100)

    keywords = models.ManyToManyField(Keyword)

    def kwds(self):
        return ','.join(k.phrase for k in self.keywords.all())

    def __unicode__(self):
        return '%s - %s' % (self.title, self.url)

class MenuItem(models.Model):
    class Meta:
        verbose_name = u'раздел меню'
        verbose_name_plural = u'Разделы меню'
    title = models.CharField(u'Заголовок', max_length=100)
    position = models.IntegerField(u'Позиция')
    page = models.OneToOneField(Page)

    def __unicode__(self):
        return self.title
