from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)

    def __str__(self) -> str:
        return self.email

class Post(models.Model):

    POST_TYPES = [('c', "copyright"), ('p', "public")]
    TITLE_MAX_LENGTH = 250

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
