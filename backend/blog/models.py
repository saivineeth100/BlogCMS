from django.db import models
from django.conf import settings


class BlogStatuses(models.TextChoices):
    PUBLISHED = 'Published', _('Published')
    DRAFT = 'Draft', _('Draft')


class Publishmanager(models.Manager):

    # Get all published posts
    def get_queryset(self):
        return super(Publishmanager, self).get_queryset().filter(status=BlogStatuses.PUBLISHED)


class BlogPost(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=10, choices=BlogStatuses.choices, default=BlogStatuses.DRAFT)
    author = models.ForeignKey(to='users.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    altered_on = models.DateField(auto_now_add=True)
    objects = models.Manager()
    published = Publishmanager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class BlogPost_Review(BlogPost):
    baseid = models.ForeignKey(to=BlogPost,on_delete=models.CASCADE,related_name='changesunderreview')



