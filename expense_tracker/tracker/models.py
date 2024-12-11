from django.db import models

# Create your models here.

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food','Food'),
        ('Transport','Transport'),
        ('Utilities','Utilities'),
        ('Others','Others'),
    ]

    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.categoty}: {self.amount}'