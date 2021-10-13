from django.db import models
from django.utils.timezone import now

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    editora = models.CharField(max_length=30)
    foto = models.URLField()
    autores = models.JSONField()
    created_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.titulo