from django.db import models
from django.urls import reverse
from datetime import date

CLEAN = (
    ('W', 'Wax'),
    ('P', 'Polish'),
    ('S', 'Shine'),
)

class Owner(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('owners_detail', kwargs={'pk': self.id})


class Ring(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    owners = models.ManyToManyField(Owner)

    def cleaned_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(CLEAN)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ring_id': self.id})
    
class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    cleaning = models.CharField(
        max_length=1,
        choices=CLEAN,
        default=CLEAN[0][0],
    )
    
    ring = models.ForeignKey(
        Ring,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_cleaning_display()} on {self.date}"
