from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    cost = models.SmallIntegerField()
    price = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.BigIntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.TextField()
    payment_type = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name} - {'Paid' if self.payment_type else 'Pending'}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_products")
    count = models.PositiveSmallIntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.order.customer.first_name} - {self.product.title} x {self.count}"
