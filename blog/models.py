from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    Email = models.EmailField( max_length=254)


    def __str__(self):
        return self.first_name




class Post(models.Model):
    Title = models.CharField( max_length=150)
    Excerpt = models.CharField( max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    Date = models.DateField(auto_now=True)
    Slug = models.SlugField(unique=True,db_index=True)
    Content = models.TextField(validators=[MinLengthValidator(10)])
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="Posts")
    Tag = models.ManyToManyField(Tag)


