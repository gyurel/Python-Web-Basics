from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
# from expenses_tracker.settings import BASE_DIR
from expenses_tracker.web.validators import only_letters_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_MB = 5
    IMAGE_UPLOAD_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )
    )

    profile_image = models.ImageField(
        # default=f'{BASE_DIR}/staticfiles/user.png',
        upload_to=IMAGE_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_MB),
        )

    )


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField(
        verbose_name='Link to image',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
