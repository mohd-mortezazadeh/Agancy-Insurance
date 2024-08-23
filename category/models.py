from tabnanny import verbose

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import OrganizedMixin
from painless.models.validations import (validate_file_extension,
                                         validate_file_size)


class Category(OrganizedMixin):
    icon = models.CharField(_("ایکن"), max_length=128, blank = True, null = True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='subcategory', verbose_name="زیر مجموعه")
    banner=models.ImageField(_('تصویر'),
        upload_to='category/%Y/%m/%d', blank=True, validators=[validate_file_extension, validate_file_size])
    content = RichTextField(_('پیام'),blank=True,null=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندیها'
    
    def __str__(self):
        return self.title

    def children(self):
        return Category.objects.filter(parent=self)


    @property
    def is_parent(self):
        """Return `True` if instance is a parent."""
        if self.parent is not None:
            return False
        return True

    def get_absolute_url(self):
        return reverse('blog:detail_by_category_slug', kwargs={"slug": self.slug})


    def posts_base_on_category(self):
        return reverse('category:posts_list_by_category', kwargs={"slug": self.slug})
    