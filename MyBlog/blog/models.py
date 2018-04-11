
from django.db import models
from datetime import datetime

# Create your models here.


# 首页
class UserProfile(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50, default='')
    content = models.TextField(verbose_name='内容', help_text='博客内容')
    pub = models.DateField(verbose_name='发布时间', default=datetime.now)
    image = models.ImageField(verbose_name='首页图片', upload_to='first/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '博客首页'
        verbose_name_plural = verbose_name
        ordering = ['-pub']

    def __str__(self):
        return self.title


# 学无止境
class LearnProfile(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50, default='')
    content = models.TextField(verbose_name='内容', help_text='板块内容')
    pub = models.DateField(verbose_name='发布时间', default=datetime.now)
    image = models.ImageField(verbose_name='学习图片', upload_to='learn/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '学无止境'
        verbose_name_plural = verbose_name
        ordering = ['-pub']

    def __str__(self):
        return self.title


# 故事与酒
class LifeProfile(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50, default='')
    content = models.TextField(verbose_name='内容', help_text='板块内容')
    pub = models.DateField(verbose_name='发布时间', default=datetime.now)
    image = models.ImageField(verbose_name='生活图片', upload_to='life/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '故事与酒'
        verbose_name_plural = verbose_name
        ordering = ['-pub']

    def __str__(self):
        return self.title


# 关于我
class AboutMe(models.Model):
    content = models.TextField(verbose_name='内容', help_text='我的故事')

    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = verbose_name
