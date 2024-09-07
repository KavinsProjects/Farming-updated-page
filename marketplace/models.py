from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('vegetable','Vegetable'),
        ('fruit','Fruit'),
        ('crop','Crop'),
    ]
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    discount_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    category = models.CharField(max_length=100,default='uncategorized')
    product_type = models.CharField(max_length=100,choices=PRODUCT_TYPE_CHOICES, default='vegetable')
    image = models.ImageField(upload_to='product_images/',null = True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.user.username}"


class Request(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    accept = models.BooleanField(default=False)

    def __str__(self):
        return f"Request by {self.buyer.user.username} for {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.product.name} by {self.buyer.user.username}"
'''
class Contract(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    contract_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField()
    payment_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')

    def __str__(self):
        return f"Contract between {self.farmer} and {self.buyer} for {self.crop}"
'''