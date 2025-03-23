from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='club_logos/', null=True, blank=True)  # Allow null and blank
    gallery = models.ManyToManyField('ClubImage', blank=True, related_name='club_gallery')

    def __str__(self):
        return self.name

class ClubImage(models.Model):
    image = models.ImageField(upload_to='club_gallery/')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_images')

    def __str__(self):
        return f"Image for {self.club.name}"