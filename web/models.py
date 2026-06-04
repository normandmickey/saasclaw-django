from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name or f'Employee #{self.pk}')

