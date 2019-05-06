from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.TextField()
    cover = models.ImageField(upload_to='images/')
    category = models.OneToOneField(
        Category,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.name
