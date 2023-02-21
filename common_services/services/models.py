from django.db import models
from django.shortcuts import reverse


class Categories(models.Model):
    name = models.CharField(db_index=True, max_length=150)
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('services:categories', kwargs=kwargs)

    class Meta:
        db_table = 'categories'


class Rooms(models.Model):
    room = models.IntegerField(db_index=True)

    def __str__(self):
        return str(self.room)

    class Meta:
        db_table = 'rooms'


class Services(models.Model):
    categories_fk = models.ForeignKey(Categories,
                                      on_delete=models.CASCADE,
                                      related_name='services_categories')
    room_fk = models.ForeignKey(Rooms,
                                on_delete=models.CASCADE,
                                related_name='services_room')
    link = models.CharField(unique=True, max_length=800)
    description = models.TextField()

    def __str__(self):
        return self.link

    class Meta:
        db_table = 'services'
