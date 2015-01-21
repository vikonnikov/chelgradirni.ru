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
        verbose_name = u'�������� �����'
        verbose_name_plural = u'�������� �����'

    phrase = models.CharField(max_length=100)

    def __unicode__(self):
        return self.phrase

class Page(models.Model):
    class Meta:
        verbose_name = u'��������'
        verbose_name_plural = u'��������'

    title = models.CharField(u'���������', max_length=100,)
    url = models.CharField(u'������', max_length=100)
    content = models.TextField(u'����������')
    description = models.TextField(u'��������', max_length=100)

    keywords = models.ManyToManyField(Keyword)

    def kwds(self):
        return ','.join(k.phrase for k in self.keywords.all())

    def __unicode__(self):
        return '%s - %s' % (self.title, self.url)

class MenuItem(models.Model):
    class Meta:
        verbose_name = u'������ ����'
        verbose_name_plural = u'������� ����'
    title = models.CharField(u'���������', max_length=100)
    position = models.IntegerField(u'�������')
    page = models.OneToOneField(Page)

    def __unicode__(self):
        return self.title
