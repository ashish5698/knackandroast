from django.db import models

# Create your models here.

class Cake(models.Model):
    cake_title = models.CharField(max_length=200)
    cake_content = models.TextField()
    cake_id = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='main/',null=True)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.cake_title
