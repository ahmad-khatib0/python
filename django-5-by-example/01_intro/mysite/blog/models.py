from django.db import models
from django.utils import timezone
from django.db.models.functions import Now
from django.conf import settings


# There are two ways to add or customize managers for your models: you can add extra manager methods
# to an existing manager or create a new manager by modifying the initial QuerySet that the manager
# returns. The first method provides you with a QuerySet notation like Post.objects.my_manager(),
# and the latter provides you with a QuerySet notation like Post.my_manager.all().
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):
    # save posts as a draft until ready for publication
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # or using database-computed default values. Introduced in Django 5,, To use
    # database-generated default values, we use the db_default attribute instead of default
    # publish = models.DateTimeField(db_default=Now())

    # auto_now_add, the date will be saved automatically when creating an object.
    created = models.DateTimeField(auto_now_add=True)
    # auto_now, the date will be updated automatically when saving an object.
    updated = models.DateTimeField(auto_now=True)

    # status is enum, so you can Status.values, Status.labels, ...
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    # We use related_name to specify the name of the reverse relationship, from User to Post.
    # This will allow us to access related objects easily from a user object by using the
    # user.blog_posts notation.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )

    # Defining a default sort order
    class Meta:
        ordering = ["-publish"]
        # define the index specifically in descending order
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.title
