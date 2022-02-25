from django.db import models

# Create your models here.


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    image_url = models.URLField()


class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MEX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=TYPE_MEX_LENGTH,
    )
