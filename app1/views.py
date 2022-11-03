from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    liste_computer = Computer.objects.all()
    antwort = []
    for einzel_computer in liste_computer:
        rechner = []
        rechner.append((einzel_computer,einzel_computer.standort, f"{einzel_computer.id:08}"))
        liste_arbeitsspeicher = Arbeitsspeicher.objects.filter(computer=einzel_computer)
        summe = 0
        as_liste = []
        anzahl = 0
        for arbeitsspeicher in liste_arbeitsspeicher:
            as_liste.append((arbeitsspeicher, arbeitsspeicher.id))
            summe += arbeitsspeicher.speichertyp.groesse
            anzahl += 1
        rechner.append(as_liste)
        rechner.append(summe)
        rechner.append(anzahl)
        liste_massenspeicher = Massenspeicher.objects.filter(computer=einzel_computer)
        ms_liste = []
        anzahl = 0
        for massenspeicher in liste_massenspeicher:
            ms_liste.append((massenspeicher, massenspeicher.id))
            anzahl += 1
        rechner.append(ms_liste)
        rechner.append(anzahl)
        liste_nic = NIC.objects.filter(computer=einzel_computer)
        nic_liste = []
        anzahl = 0
        for nic in liste_nic:
            nic_liste.append((nic.mac, nic.id))
            anzahl += 1
        rechner.append(nic_liste)
        rechner.append(anzahl)

        antwort.append(rechner)
    #print(antwort)    
    return render(request, 'app1/liste_comp.html', {'rechner': antwort})
