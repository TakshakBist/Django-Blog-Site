from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # if user is deleted, profile pic is deleted, not vice-versa
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')  # install pillow

    def __str__(self):
        return f'{self.user.username} Profile'

    # overriding save function to resize image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


