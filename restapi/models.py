from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

from io import BytesIO
from PIL import Image

full_url = 'http://127.0.0.1:8000'


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avg_review = models.CharField(max_length=10, blank=True, null=True)
    review_count = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return full_url + self.image.url
        return ''

    # def get_thumbnail(self):
    #     if self.image:
    #         return full_url + self.image.url
    #     else:
    #         if self.image:
    #             self.image = self.make_thumbnail(self.image)
    #             self.save()
    #
    #             return full_url + self.image.url
    #         else:
    #             return ''
    #
    # def make_thumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #
    #     img.convert('RGB')
    #     img.thumbnail(size)
    #
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)
    #
    #     image = File(thumb_io, name=image.name)
    #
    #     return image

    def __str__(self):
        return self.title
