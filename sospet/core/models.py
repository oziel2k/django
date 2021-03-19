from django.db.models.deletion import CASCADE
from sospet.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models
from django.db.models.fields.related import ForeignObject
from django.contrib.auth.models import User

class Pet(models.Model):
    cidade          = models.CharField(max_length=100)
    descricao       = models.TextField()
    telefone        = models.CharField(max_length=20)
    email           = models.EmailField()
    datacriacao     = models.DateTimeField(auto_now_add=True)    
    ativo           = models.BooleanField(default=True)
    usuario         = models.ForeignKey(User,on_delete=models.PROTECT)
    foto            = models.ImageField(upload_to='pet', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
            db_table = "pet"