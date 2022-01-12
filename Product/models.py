from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return '%s | %s' % (self.name, self.price)
    
    