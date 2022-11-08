from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import check_rel_lookup_compatibility
from django.utils import timezone

# Create your models here.
class Ort(models.Model):
    ort = models.CharField(max_length=50, verbose_name="Ort")
    def __str__(self):
        return f"{self.ort}"
    class Meta:
        verbose_name_plural = "Orte"
        verbose_name = "Ort"

class Raum(models.Model):
    ort = models.ForeignKey(Ort, on_delete=models.RESTRICT,verbose_name="Ort")
    raum = models.CharField(max_length=50, verbose_name="Raum")   
    def __str__(self):
        return f"{self.raum} - {self.ort}"
    class Meta:
        verbose_name_plural = "Räume"
        verbose_name = "Raum"
    
class Standort(models.Model):
    raum = models.ForeignKey(Raum, on_delete=models.RESTRICT,verbose_name="Raum")
    bezeichnung = models.CharField(max_length=50, verbose_name="Standort")   
    def __str__(self):
        return f"{self.bezeichnung} - {self.raum}"
    class Meta:
        verbose_name_plural = "Standorte"
        verbose_name = "Standort"

class Prozessor(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")
    takt =  models.CharField(max_length=10, verbose_name="Takt")
    anzahl_kerne = models.IntegerField(verbose_name="Anzahl Kerne")
    anzahl_kerne_logisch = models.IntegerField(verbose_name="Anzahl logischer Kerne", default=0)
    def __str__(self):
        return f"{self.bezeichnung}/{self.takt} ({self.anzahl_kerne})"
    class Meta:
        verbose_name_plural = "Prozessoren"
        verbose_name = "Prozessor"

class Hersteller(models.Model):
    hersteller = models.CharField(max_length=50, verbose_name="Hersteller")
    def __str__(self):
        return f"{self.hersteller}"
    class Meta:
        verbose_name_plural = "Hersteller"
        verbose_name = "Hersteller"

class Computer(models.Model):
    standort = models.ForeignKey(Standort, on_delete=models.RESTRICT,verbose_name="Standort")
    prozessor = models.ForeignKey(Prozessor, on_delete=models.RESTRICT,verbose_name="Prozessor")
    hersteller = models.ForeignKey(Hersteller, on_delete=models.RESTRICT,verbose_name="Hersteller")

    # Zusatzfelder
    product = models.CharField(max_length=50, verbose_name="Produkt", blank = True)
    modell = models.CharField(max_length=50, verbose_name="Modell", blank = True)
    seriennummer = models.CharField(max_length=50, verbose_name="SN", blank = True)
    zusatzinfo = models.CharField(max_length=50, verbose_name="Zusatzinfo", blank = True)
    pin = models.CharField(max_length=50, verbose_name="PIN", default='000000')
    def __str__(self):
        return f"C{self.id:08}/{self.prozessor.bezeichnung} - {self.hersteller}"
    class Meta:
        verbose_name_plural = "Computer"
        verbose_name = "Computer"
    
class Einsatzgebiet(models.Model):
    slug = models.CharField(max_length=50,primary_key=True, verbose_name="Abkürzung")
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")
    def __str__(self):
        return f"{self.slug}/{self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Einsatzgebiete"
        verbose_name = "Einsatzgebiet" 

class Einsatzmoeglichkeit(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.RESTRICT,verbose_name="Computer")
    einsatzgebiet = models.ForeignKey(Einsatzgebiet, on_delete=models.RESTRICT,verbose_name="Einsatzgebiet")
    def __str__(self):
        return f"{self.computer}/{self.einsatzgebiet}"
    class Meta:
        verbose_name_plural = "Einsatzmöglichkeit"
        verbose_name = "Einsatzmöglichkeit" 


class Sorte(models.Model):
    Bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung") 
    def __str__(self):
        return f"{self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Sorten"
        verbose_name = "Sorte"
    
class Anschlusstyp(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")
    slug = models.CharField(max_length=50, verbose_name="Anschlusstyp") 
    def __str__(self):
        return f"{self.slug}"
    class Meta:
        verbose_name_plural = "Anschlusstypen"
        verbose_name = "Anschlusstyp"

class Speicherart(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")
    slug = models.CharField(max_length=50, verbose_name="Typ") 
    def __str__(self):
        return f"{self.slug}"
    class Meta:
        verbose_name_plural = "Massenspeicherarten"
        verbose_name = "Massenspeicherart"

class Massenspeichertyp(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")
    anschluss = models.ForeignKey(Anschlusstyp, on_delete=models.RESTRICT, verbose_name="Anschluss")
    typ = models.ForeignKey(Speicherart, on_delete=models.RESTRICT, verbose_name="Speicherart")
    groesse = models.CharField(max_length=50, verbose_name="Größe")
    def __str__(self):
        return f"{self.bezeichnung}/{self.typ}/{self.anschluss}/{self.groesse}"
    class Meta:
        verbose_name_plural = "Massenspeichertypen"
        verbose_name = "Massenspeichertyp"

class Massenspeicher(models.Model):
    speichertyp = models.ForeignKey(Massenspeichertyp, on_delete=models.RESTRICT)
    hersteller = models.ForeignKey(Hersteller, on_delete=models.RESTRICT,verbose_name="Hersteller")
    seriennummer = models.CharField(max_length=50, verbose_name="SN", blank=True)
    computer = ForeignKey(Computer, on_delete=models.RESTRICT, verbose_name="Computer", blank=True, null=True)
    comment = models.CharField(max_length=50, verbose_name="Kommentar", blank=True)

    def __str__(self):
        return f"MS{self.id:06} - {self.speichertyp}"
    class Meta:
        verbose_name_plural = "Massensspeicher"
        verbose_name = "Massensspeicher"

class Arbeitsspeichertyp(models.Model):
    typ = models.CharField(max_length=50, verbose_name="Typ")
    groesse = models.IntegerField(verbose_name="Größe in GB")
    takt = models.CharField(max_length=50, verbose_name="Takt")
    ecc = models.BooleanField(verbose_name="ECC tauglich")
    def __str__(self):
        return f"{self.typ}/{self.groesse} GB/{self.takt}"
    class Meta:
        verbose_name_plural = "Arbeitsspeichertypen"
        verbose_name = "Arbeitsspeichertyp"

class Arbeitsspeicher(models.Model):
    speichertyp = models.ForeignKey(Arbeitsspeichertyp, on_delete=models.RESTRICT) 
    computer = models.ForeignKey(Computer, on_delete=models.RESTRICT, verbose_name="Computer", blank = True, null = True)
    hersteller = ForeignKey(Hersteller, on_delete=models.RESTRICT, verbose_name="Hersteller")
    seriennummer = models.CharField(max_length=50, verbose_name="SN", null=True)
    def __str__(self):
        return f"AS{self.id:06} - {self.speichertyp} "
    class Meta:
        verbose_name_plural = "Arbeitsspeicher"
        verbose_name = "Arbeitsspeicher"

class NICTyp(models.Model):
    typ = models.CharField(max_length=50, verbose_name="NIC Typ")
    bezeichnung = models.CharField(max_length=50, verbose_name="Bezeichnung")    
    def __str__(self):
        return f"{self.typ}"
    class Meta:
        verbose_name_plural = "NIC Typen"
        verbose_name = "NIC Typ"

class NIC(models.Model):
    typ = models.ForeignKey(NICTyp, on_delete=models.RESTRICT,verbose_name="Typ")
    computer = models.ForeignKey(Computer, on_delete=models.RESTRICT, verbose_name="Computer", null = True, blank=True)
    mac = models.CharField(max_length=50, verbose_name="MAC Adresse")
    kommentar =  models.CharField(max_length=50, verbose_name="Kommentar", blank = True)
    def __str__(self):
        return f"NIC{self.id:06} - {self.typ}/[{self.mac}]"
    class Meta:
        verbose_name_plural = "NIC"
        verbose_name = "NIC"

class ToolTyp(models.Model):
    typ = models.CharField(max_length=50, verbose_name="ToolTyp ")
    kommentar =  models.CharField(max_length=50, verbose_name="Kommentar", blank = True)
    def __str__(self):
        return f"{self.typ}"
    class Meta:
        verbose_name_plural = "Tooltyp"
        verbose_name = "Tooltypen"


class Tool(models.Model):
    standort = models.ForeignKey(Standort, on_delete=models.RESTRICT,verbose_name="Standort")
    type = models.ForeignKey(ToolTyp, on_delete=models.RESTRICT,verbose_name="Typ")
    # Zusatzfelder
    computer = models.ForeignKey(Computer, on_delete=models.RESTRICT, verbose_name="Computer", null = True, blank=True)
    zusatzinfo = models.CharField(max_length=50, verbose_name="Zusatzinfo", blank = True)
    def __str__(self):
        return f"T{self.id:08}/{self.type}/{self.standort}"
    class Meta:
        verbose_name_plural = "Tools"
        verbose_name = "Tool"

