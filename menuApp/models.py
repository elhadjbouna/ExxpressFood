from django.db import models

# Create your models here.

class Plat(models.Model):
    PlatId = models.AutoField(primary_key=True)
    PlatName= models.CharField(max_length=500)
    Price= models.IntegerField(default=5)
    image = models.CharField(max_length=500,default='images/Ratatouille_001.jpg')

class CarteDuJour(models.Model):
    CarteDuJjourId = models.AutoField(primary_key=True)
    Plat = models.CharField(max_length=500)
    DateOfCreation = models.DateField()
    PhotoFile= models.CharField(max_length=500)
    image = models.CharField(max_length=500,default='images/Ratatouille_001.jpg')
    Jours = models.CharField(max_length=500,default='Lundi')



class Desert(models.Model):
    DesertId = models.AutoField(primary_key=True)
    DesertName = models.CharField(max_length=500)
    Price= models.IntegerField(default=2)
    image = models.CharField(max_length=500,default='images/Ratatouille_001.jpg')

class Livreur(models.Model):
    LivreurId = models.AutoField(primary_key=True)
    LivreurName = models.CharField(max_length=500)
    LivreurPrenom = models.CharField(max_length=500)

class Commande(models.Model):
    CommandeId = models.AutoField(primary_key=True)
    CommandeName = models.CharField(max_length=500)
    Plat = models.CharField(max_length=500)
    Desert = models.CharField(max_length=500)
    Livreur = models.CharField(max_length=500)
    

    

class Personne(models.Model):
    PersonneId = models.AutoField(primary_key=True)
    PersonneName = models.CharField(max_length=500)
    PersonnePrenom = models.CharField(max_length=500)
    type = models.CharField(max_length=500)



class Client(models.Model):
    ClientId = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length=500)
    ClientPrenom = models.CharField(max_length=500)
    ClientAdress = models.CharField(max_length=500,default='Ruil')



