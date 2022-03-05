from django.db import models

# Create your models here.
from my_music_app.web.validators import min_length_validator, below_zero_validator, \
    only_letters_numbers_underscore_validator


class Profile(models.Model):
    USER_NAME_MAX_LENGTH = 15
    USER_NAME_MIN_LENGTH = 2

    user_name = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        validators=(
            min_length_validator,
            only_letters_numbers_underscore_validator,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            below_zero_validator,
        )
    )


class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=[
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other"),
        ]
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            below_zero_validator,
        )
    )
