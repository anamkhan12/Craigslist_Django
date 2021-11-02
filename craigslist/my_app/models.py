from django.db import models

class Search(models.Model):
    search = models.CharField(max_length =500)
    created_at =models.DateTimeField(auto_now=True)
    
    
    class Meta :
        verbose_name_plural = 'Searches'