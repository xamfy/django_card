from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Pic(models.Model):

    ROBOTO = 'Roboto'
    ZCOOL = 'ZCOOL'
    FONT_CHOICES = (
        (ROBOTO, 'Roboto'),
        (ZCOOL, 'ZCOOL'),
    )

    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    blank = models.ImageField(upload_to='images/blanks/')

    category = models.ForeignKey(
        Category,
        related_name='images',
        on_delete=models.DO_NOTHING,
    )
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    font = models.CharField(
        max_length=100,
        choices=FONT_CHOICES,
        default=ROBOTO,
    )

    size = models.IntegerField(default=10)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name
