from rest_framework import serializers
from .models import Osoba, Druzyna, MIESIAC_URODZENIA

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=MIESIAC_URODZENIA.choices, default=MIESIAC_URODZENIA.choices[0][0])
    kraj = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance