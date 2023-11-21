from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.category.delete()
        super().delete(*args, **kwargs)

    def get_category_hierarchy(self):
        category_hierarchy = []
        category = self.category
        while category is not None:
            category_hierarchy.append(category.title)
            category = category.parent
        return ' · '.join(reversed(category_hierarchy))
