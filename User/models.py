from django.contrib.auth.models import AbstractUser

from Product.models import Product


class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username
    
    
    def get_products(self) -> list:
        return self.product_set.all()
    
    
    def get_product(self, id) -> object:
        return self.product_set.get(id=id)
    
    
    def set_product(self, name, price) -> None:
        Product.objects.create(
            name=name,
            price=price,
            user=self,
        )
        