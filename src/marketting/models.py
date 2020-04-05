from django.db import models

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.TimeField(auto_now=True)

    def __str__(self):
        return self.email