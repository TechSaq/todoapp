from django.db import models

class ToDo(models.Model):
    
    CATEGORY_CHOICES = (
        ('H', 'Home'),
        ('W', 'Work'),
        ('P', 'Play'),
        ('N', 'Normal')
    )

    description = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="SELECT CATEGORY")
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    due_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.description
