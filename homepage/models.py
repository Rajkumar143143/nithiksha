from django.db import models

# Create your models here.
class item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_des = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://images.unsplash.com/photo-1471107340929-a87cd0f5b5f3?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Ym9vayUyMHBlbnxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80")

