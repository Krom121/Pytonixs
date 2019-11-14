from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField




class NewClient(models.Model):
    WEBSITE_NEEDED = (
        ('brochure_website', 'Brochure Website'),
        ('blog_website', 'Blog Website'),
        ('portfolio_website', 'Portfolio Website'),
        ('business_website', 'Business Website'),
        ('e-commerce_website','E-commerce Website'),
        ('other', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    current_website = models.CharField(max_length=100)
    website_needed = models.CharField(max_length=50, choices= WEBSITE_NEEDED, default=None)
    tell_us_more = models.TextField()


    def __str__(self):
        return self.first_name