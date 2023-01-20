from django.db import models
from django.urls import reverse


class Detect(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ady')
    surname = models.CharField(max_length=150, verbose_name='Familyasy')
    time_in = models.DateTimeField(verbose_name='Giren wagty', auto_now=True)
    time_out = models.DateTimeField(verbose_name='Cykan wagty', auto_now=True)
    photo = models.ImageField(upload_to='product-img/', verbose_name='Suraty', blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Wezipesi')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detect_form', kwargs={"pk": self.pk})


    class Meta:
        verbose_name = 'Hasaba almak'
        ordering = ['name']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Wezipesi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Wezipesi'
        verbose_name_plural = 'Wezipesi'
        ordering = ['title']
