>>> from polls.models import Osoba
>>> from polls.serializers import OsobaSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> osoba = Osoba(imie='Dominik', nazwisko='Kownacki', miesiac_urodzenia=7)  
>>> osoba.save()
>>> serializer = OsobaSerializer(osoba)
>>> serializer.data
{'id': 4, 'imie': 'Dominik', 'nazwisko': 'Kownacki', 'miesiac_urodzenia': '7', 'kraj': None}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":4,"imie":"Dominik","nazwisko":"Kownacki","miesiac_urodzenia":"7","kraj":null}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = OsobaSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.validated_data
OrderedDict([('imie', 'Dominik'), ('nazwisko', 'Kownacki'), ('miesiac_urodzenia', '7'), ('kraj', None)])
>>> deserializer.save()
<Osoba: Dominik Kownacki>
> >>> from polls.models import Druzyna
>>> from polls.serializers import DruzynaSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> druzyna = Druzyna('EN', 'Arsenal Londyn();') 
>>> druzyna.save()                                 
>>> serializer = DruzynaSerializer(druzyna)
>>> serializer.data
{'id': 1, 'kraj': 'EN', 'nazwa': 'Arsenal Londyn();'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":1,"kraj":"EN","nazwa":"Arsenal Londyn();"}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = DruzynaSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.validated_data
OrderedDict([('kraj', 'EN'), ('nazwa', 'Arsenal Londyn();')])
>>> deserializer.save()
<Druzyna: Arsenal Londyn(); (EN)>
>>> deserializer.data
{'id': 3, 'kraj': 'EN', 'nazwa': 'Arsenal Londyn();'}

