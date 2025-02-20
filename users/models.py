from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Users(models.Model):
    name = models.TextField(blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)  # Store hashed passwords

    def save(self, *args, **kwargs):
        """Hash the password before saving a new user"""
        if not self.pk:  # Only hash when creating a new user
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Check if the password matches the hashed password"""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name