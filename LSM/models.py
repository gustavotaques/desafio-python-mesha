from django.db import models

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    editora = models.CharField(max_length=30)
    foto = models.URLField()
    autores = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo