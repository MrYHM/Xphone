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
    extra = models.CharField(max_length=20,null=True,blank=True)


    class Meta():
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ProductName.encode('utf-8')


#