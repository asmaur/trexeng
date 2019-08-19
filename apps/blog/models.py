from django.db import models
import uuid, os
from django.conf import settings
from imagekit.processors import ResizeToFit
from imagekit.models import ProcessedImageField
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.dispatch import receiver
from .processors import Watermark


# Create your models here.

def change_name(filename):
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4().hex, ext)
    return filename

def path_post(instance, filename):
# file will be uploaded to MEDIA_ROOT/company_<name>/

    return 'WANUCLOUD/posts/{0}/{1}'.format(instance.code, change_name(filename))

def image_path_post(instance, filename):
# file will be uploaded to MEDIA_ROOT/company_<name>/shop_<name>/
    parent_path = instance.post._meta.get_field('capa').upload_to(instance.post, '')
    #print(parent_path)
    return 'WANUCLOUD/posts/{0}/{1}'.format(instance.post.code, change_name(filename))


def generate_uid():
    return str(uuid.uuid4().fields[-1])[:7]




class Post(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    projeto = models.CharField(max_length=50, help_text="tipo de projeto", blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    capa = ProcessedImageField(upload_to=path_post, processors=[ResizeToFit(720, 405), Watermark(text="TREX ENGENHARIA")], format='JPEG', options={'quality': 60}, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.code

    def delete(self, *args, **kwargs):
        # self.capa.delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, self.capa.name))
        super(Post, self).delete(*args, **kwargs)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    trex_img = ProcessedImageField(upload_to=image_path_post, processors=[ResizeToFit(720, 405), Watermark(text="TREX ENGENHARIA")], format='JPEG', options={'quality': 60}, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return "Image de: {0}".format(self.post.code)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.trex_img.name))
        super(Image, self).delete(*args, **kwargs)


@receiver(pre_save, sender=Post)
def post_pre_save(sender, **kwargs):
    post = kwargs.get('instance')

    if not post.code:
        post.code = generate_uid()

    if not post.slug:
        post.slug = slugify(post.title)
