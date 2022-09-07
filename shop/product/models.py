from django.db import models

CATEGORY = [
    ('', 'Category'),
    ('Cartoon', 'Cartoon'),
    ('Documentary', 'Documentary'),
    ('Action', 'Action')
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey('Product_type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'


class Product_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_type'


class Notebook(models.Model):
    name = models.CharField(max_length=255)
    memory_type = models.ForeignKey('Memory_type', on_delete=models.CASCADE)
    cpu_type = models.ForeignKey('Cpu_type', on_delete=models.CASCADE)
    video_type = models.ForeignKey('Video_type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notebook'


class Memory_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'memory_type'


class Video_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'video_type'


class Cpu_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'cpu_type'