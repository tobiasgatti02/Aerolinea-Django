from django.db import models

class Aeropuerto(models.Model):
    codigo = models.CharField(max_length =3)
    ciudad = models.CharField(max_length = 64)

    def __str__(self)-> str:
        return f"{self.ciudad} ({self.codigo})"

# Create your models here.
class Vuelo(models.Model):
    origen = models.ForeignKey(Aeropuerto,on_delete=models.CASCADE, related_name="salidas")
    destino = models.ForeignKey(Aeropuerto,on_delete=models.CASCADE, related_name="arribos")
    duracion = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}:{self.origen} a {self.destino}"
    

