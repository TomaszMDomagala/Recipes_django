from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
from django.urls import reverse

class Recipes(models.Model):
    name = models.CharField(max_length = 200)
    add_date = models.DateField(auto_now_add=True)
    ingredients = models.TextField()
    description = models.TextField()
    rating = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='food_pics')

    class Foods(models.TextChoices):
        SNIADANIA = "Śniadania"
        LUNCHE = "Lunche"
        ZUPY = "Zupy"
        SALATKI = "Sałatki"
        SUROWKI = "Surówki"
        CIASTA = "Ciasta"
        OBIADY = "Obiady"
        DODATKI = "Dodatki"
        PODWIECZORKI = "Podwieczorki"
        KOLACJE = "Kolacje"

    type = models.CharField(
        max_length=12,
        choices=Foods.choices,
    )

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
      verbose_name_plural = "Recipes"
