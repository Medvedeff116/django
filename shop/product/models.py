from django.db import models
from pyaml import unicode

CATEGORY = [
    ('', 'Category'),
    ('Cartoon', 'Cartoon'),
    ('Documentary', 'Documentary'),
    ('Action', 'Action')
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey('Product_type', on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name ='Продукты'
        verbose_name_plural ='Продукты'


class Product_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_type'


class Notebook(models.Model):
    name = models.CharField(max_length=255,verbose_name='Наименование')
    memory_type = models.ForeignKey('Memory_type', on_delete=models.CASCADE, verbose_name='Оперативная память')
    cpu_type = models.ForeignKey('Cpu_type', on_delete=models.CASCADE,verbose_name='Процессор')
    video_type = models.ForeignKey('Video_type', on_delete=models.CASCADE,verbose_name='Видеокарта')

    def __unicode__(self):
        return u'%s - %s' % (self.memory_type,self.name)
    class Meta:
        db_table = 'notebook'
        verbose_name = 'Ноутбуки'
        verbose_name_plural = 'Ноутбуки'



        def __str__(self):
            fields =[self.name]
            result= " ".join(list(filter(lambda x:x, fields)))
            return result or ''




class Memory_type(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return (self.name)

    def __str__(self):
        fields = [self.name]
        result = " ".join(list(filter(lambda x: x, fields)))
        return result or ''

    class Meta:
        db_table = 'memory_type'
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'


class Video_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        fields = [self.name]
        result = " ".join(list(filter(lambda x: x, fields)))
        return result or ''
    class Meta:
        db_table = 'video_type'
        verbose_name = 'Видеокарты'
        verbose_name_plural = 'Видеокарты'


class Cpu_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        fields = [self.name]
        result = " ".join(list(filter(lambda x: x, fields)))
        return result or ''
    class Meta:
        db_table = 'cpu_type'
        verbose_name = 'Процессоры'
        verbose_name_plural = 'Процессоры'

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=1024)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):  return str(self.username)


