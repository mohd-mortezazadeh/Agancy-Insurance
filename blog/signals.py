import os

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from blog.models import Post


@receiver(post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.banner:
        if os.path.isfile(instance.banner.path):
            os.remove(instance.banner.path)


@receiver(pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Post.objects.get(pk=instance.pk).banner
    except Post.DoesNotExist:
        return False
    if not old_file:
        return
    new_file = instance.banner
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



@receiver(pre_save,sender=Post)
def create_post(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_uniqe_slug(instance)


def create_uniqe_slug(instance,newslug=None):
    if newslug is not None:
        slug=newslug
    else:
        slug=slugify(instance.title,allow_unicode=True)

    instanClass=instance.__class__
    qs=instanClass.objects.filter(slug=slug)

    if qs.exists():
        newslug=f"{slug}-{qs.first().pk}"
        return create_uniqe_slug(instance,newslug)

    return slug
   