from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"nick name", default="")
    birday = models.DateField(verbose_name=u"birthday", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male",u"male"),("female","female")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "User information"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    def unread_nums(self):
        #Gets the number of unread messages from the user
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()



class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"The title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"image", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"address")
    index = models.IntegerField(default=100, verbose_name=u"index")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"banner"
        verbose_name_plural = verbose_name