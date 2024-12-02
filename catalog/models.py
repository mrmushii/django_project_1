from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
  title = models.CharField(max_length= 200)
  price = models.IntegerField()
  discount_price = models.IntegerField()
  slug = models.SlugField()
  
  
  def __str__(self):
    return self.title

    



class OrderItem(models.Model):
  
  user = models.ForeignKey( User,  on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  Ordered = models.BooleanField(default=False)
  quantity = models.IntegerField(default= 1)

  def __str__(self):
    return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
  user = models.ForeignKey( User,  on_delete=models.CASCADE)
  items = models.ManyToManyField(OrderItem)
  Ordered = models.BooleanField(default=False)
  start_date = models.DateTimeField(auto_now_add=True)
  ordered_date = models.DateTimeField()
  
  
  def __str__(self):
    return self.user.username