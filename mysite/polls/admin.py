from django.contrib import admin

from .models import Question
from .models import Osoba

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)