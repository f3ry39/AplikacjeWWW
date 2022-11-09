from django.contrib import admin

from .models import Question
from .models import Osoba
from .models import Druzyna

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'kraj']
    list_filter = ['kraj', 'data_dodania']
class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ['nazwa']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)
