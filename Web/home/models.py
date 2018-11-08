from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class artical_model(models.Model):
    artical_title =  models.CharField(max_length=100, default='')#文章開頭
    artical_type =  models.CharField(max_length=100, default='')#文章屬性如:活動，公告，特價資訊等
<<<<<<< HEAD
    artical_add_date =  models.DateTimeField(default = timezone.now)#文章建立時間
=======
    artical_add_data =  models.DateTimeField(default = timezone.now)#文章建立時間
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
    artical_mod_date = models.DateTimeField(auto_now = True)#文章修改時間
    artical_content = models.TextField(blank=True, default='')#內文
    def __str__(self):
        return self.artical_title