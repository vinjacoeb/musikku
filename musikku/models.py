from django.db import models

class Musik(models.Model):
    Judul = models.CharField(max_length=255)
    Penyanyi = models.CharField(max_length=255)
    Lirik = models.TextField()

    def __str__(self):
        return self.Judul
