from rest_framework import serializers
from .models import Osoba, Druzyna, MIESIAC_URODZENIA, Question, Choice

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=MIESIAC_URODZENIA, default=MIESIAC_URODZENIA[0][0])
    kraj = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(), allow_null=True)


    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance
class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    kraj = serializers.CharField(required=True)
    nazwa = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.save()
        return instance
class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
        read_only_fields = ['id']


class ChoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']
        read_only_fields = ['id']