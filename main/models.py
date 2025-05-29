from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    color = models.CharField(max_length=50, choices=[
        ('red', 'Червоний'),
        ('blue', 'Синій'),
        ('black', 'Чорний'),
        ('white', 'Білий'),
        ('green', 'Зелений')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name