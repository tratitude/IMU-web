from django.db import models
from django.contrib import admin
from django.utils.timezone import now
class Item(models.Model):
	Name = models.CharField('商品名稱',max_length=100)
	price = models.DecimalField('商品價格',max_digits=10,decimal_places=2,default=100)
	content = models.TextField('備註',blank=True,default="")
	photo = models.URLField('照片URL',blank=True,default="")
	seller = models.CharField('賣家',max_length=100,default="")
	created_at = models.DateTimeField('更新時間',auto_now_add=True)
	
	def __str__(self):
		return self.Name
		
class ItemAdmin(admin.ModelAdmin):
    list_display = ['Name', 'price', 'seller','created_at']
    search_fields = ['Name', 'price', 'seller','created_at']
    #list_filter = ['dc_name', 'zone']
    ordering = ['price']


admin.site.register(Item, ItemAdmin)