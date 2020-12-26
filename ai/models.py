from django.db import models


class Employee(models.Model):
    name         = models.CharField(max_length=100)
    detail       = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)
        
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"
