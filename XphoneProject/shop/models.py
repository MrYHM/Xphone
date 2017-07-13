# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

#　用户表

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=11,null=True)
    addr = models.CharField(max_length=30,null=True,blank=True)
    regDate = models.DateTimeField()
    isDelete = models.BooleanField(default=False)
    extra = models.CharField(max_length=20,null=True,blank=True)


    class Meta():
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name.encode('utf-8')

# 商品种类

class ProductSort(models.Model):
    sortName = models.CharField(max_length=10)
    sortPic = models.ImageField(upload_to='uploads')


    class Meta():
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sortName.encode('utf-8')


#　商品表

class Product(models.Model):
    ProductName = models.CharField(max_length=30)
    ProductDesc = models.CharField(max_length=80)
    ProductPrice = models.DecimalField(max_digits=7,decimal_places=2)
    ProductImg = models.ImageField(upload_to='uploads/')
    saleCount = models.IntegerField(default=0)
    ProductSort = models.ForeignKey('ProductSort')
    pubdate = models.DateTimeField()
    ProductColor = models.CharField(max_length=20)
    extra = models.CharField(max_length=20,null=True,blank=True)


    class Meta():
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ProductName.encode('utf-8')


#售后

class AfterServer(models.Model):
    AfterName = models.CharField(max_length=30)
    AfterImg = models.ImageField(upload_to='uploads/')


    class Meta():
        verbose_name = '售后保障'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.AfterName.encode('utf-8')


#导航

class NavBars(models.Model):
    NavName = models.CharField(max_length=10)
    NavLog = models.ImageField(upload_to='uploads/')
    NavImg = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = "导航"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.NavName.encode('utf-8')


# 导航标签

class Navtags(models.Model):
    TagName = models.CharField(max_length=20)
    TagImg = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = '导航标签'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.TagName.encode('utf-8')

#标签详情

class TagGoods(models.Model):
    goodImg = models.ImageField(upload_to='uploads/')
    goodName = models.CharField(max_length=20)
    goodPrice = models.DecimalField(max_digits=7,decimal_places=2)
    discount = models.DecimalField(u'折扣',max_length=1,max_digits=3,decimal_places=2)
    Navtags = models.ForeignKey(Navtags,verbose_name='导航标签')

    class Meta():
        verbose_name = '标签详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goodName.encode('utf-8')

#商城广告

class Ad(models.Model):
    title = models.CharField(u'广告描述',max_length=50)
    img_url = models.ImageField(upload_to='uploads/')
    AdName = models.CharField(max_length=20)
    index = models.IntegerField(default=999)
    Navtags_id = models.ForeignKey('Navtags')
    class Meta():
        verbose_name = '商城广告'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.AdName.encode('utf-8')


#商城页商品


class ShopSales(models.Model):
    saleName = models.CharField(max_length=30)
    saleDese = models.CharField(max_length=30)
    salePrice = models.DecimalField(max_digits=5,decimal_places=2)
    saleImg = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = '商城首页商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.saleName.encode('utf-8')


#服务页

#服务内容

class ServerContent(models.Model):
    img_url = models.ImageField(u'图片',upload_to='uploads/')
    title = models.CharField(max_length=20)

    class Meta():
        verbose_name = '服务选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title.encode('utf-8')

#常见问题

class CommonProblems(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta():
        verbose_name = '常见问题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.title.encode('utf-8')


#联系我们

class Links(models.Model):
    title = models.CharField(max_length=15)
    img_url = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = '联系我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title.encode('utf-8')


#博客

class BlogAd(models.Model):
    img_url = models.ImageField(upload_to='uploads/')


    class Meta():
        verbose_name = '博客广告'
        verbose_name_plural = verbose_name


#博客导航条

class Category(models.Model):
    title = models.CharField(max_length=16)
    index = models.IntegerField(u'显示顺序',default=999)


    class Meta():
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __unicode__(self):
        return  self.title


#自定义一个文章Model管理器
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m')+'文章存档'
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    collect_count = models.IntegerField(default=0,verbose_name=u'收藏次数')

    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # tag = models.ManyToManyField(Tag, verbose_name='标签')

    # 关联管理器
    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30,blank=True,null=True,verbose_name='用户名')
    email = models.EmailField(max_length=50,blank=True,null=True,verbose_name='邮箱地址')
    url = models.URLField(max_length=100,blank=True,null=True,verbose_name='个人网址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(UserInfo, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)


#　视频模型

class Video(models.Model):
    name = models.CharField(max_length=30)
    video_url = models.CharField(u'视频资源URL',max_length=200)
    video_length = models.IntegerField(u'视频长度')

    class Meta():
        verbose_name = '视频'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.name.encode('utf-8')


#产品图片

class ProPic(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    img_url = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = "产品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title.encode('utf-8')


# 新闻　

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='新闻标题')
    desc = models.CharField(max_length=50, verbose_name='新闻描述')
    content = models.TextField(verbose_name='新闻内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(UserInfo, verbose_name='用户')
    collect_count = models.IntegerField(default=0, verbose_name=u'收藏次数')

    class Meta():
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


#OnePlus5

class OnePlusNav(models.Model):
    name = models.CharField(u'配置介绍',max_length=16)
    index = models.IntegerField(u'排序',default=999)

    class Meta():
        verbose_name = 'oneplus配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name.encode('utf-8')

#手机参数

class PhoneArg(models.Model):
    title = models.CharField(max_length=20)
    arg_desc = models.CharField(max_length=200)
    img_url = models.ImageField(upload_to='uploads/')

    class Meta():
        verbose_name = '手机参数'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class OnePlus(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    img_url = models.ImageField(upload_to='uploads/')







