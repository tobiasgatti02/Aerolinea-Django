from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
from . import Vuelo

def vuelo(request,id_vuelo):
    try:
        vuelo= Vuelo.objects.get(id_vuelo)
        return render(request,"vuelos/vuelo.html",{
            "vuelo": vuelo
        })
    except Vuelo.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))