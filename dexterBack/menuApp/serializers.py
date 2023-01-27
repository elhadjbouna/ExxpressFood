from rest_framework import serializers
from menuApp.models import Plat,CarteDuJour,Livreur,Commande,Desert,Personne,Client

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plat 
        fields=('PlatId','PlatName','Price','image')

class CarteDuJourSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarteDuJour 
        fields=('CarteDuJourId','CarteDuJourName','DateOfCreation','PhotoFile','image','Jours')

class LivreurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Livreur 
        fields=('LivreurId','LivreurName','LivreurPrenom')

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Commande 
        fields=('CommandeId','CommandeName','Plat','Desert','Livreur')

class DesertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Desert 
        fields=('DesertId','DesertName','Price','image')

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personne 
        fields=('PersonneId','PersonneName','PersonnePrenom','type')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client 
        fields=('ClientId','ClientName','ClientPrenom','ClientAdress')