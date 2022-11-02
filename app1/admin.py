from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Ort)
admin.site.register(Raum)
admin.site.register(Standort)

admin.site.register(Hersteller)
admin.site.register(Prozessor)
admin.site.register(Computer)

admin.site.register(Einsatzgebiet)
admin.site.register(Einsatzmoeglichkeit)

admin.site.register(Anschlusstyp)
admin.site.register(Speicherart)
admin.site.register(Massenspeichertyp)
admin.site.register(Massenspeicher)

admin.site.register(Arbeitsspeichertyp)
admin.site.register(Arbeitsspeicher)

admin.site.register(Sorte)

admin.site.register(NICTyp)
admin.site.register(NIC)




#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
#admin.site.register(Speichertyp)
