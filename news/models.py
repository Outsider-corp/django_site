from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title", db_index=True)
    content = models.TextField(blank=True, verbose_name="Content")
    image = models.ImageField(upload_to="photo/%Y-%m-%d/", blank=True, verbose_name="Image")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    author = models.CharField(max_length=150, verbose_name="Author")
    is_publ = models.BooleanField(default=True, verbose_name="Published")
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("view_post", kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-created_time", "title"]


class Categories(models.Model):
    title = models.CharField(max_length=150, verbose_name="Category name", db_index=True)

    def get_absolute_url(self):
        return reverse("cats", kwargs={"cat_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]
