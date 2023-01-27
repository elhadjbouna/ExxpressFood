from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from menuApp.models import Plat,CarteDuJour,Livreur,Commande,Desert,Personne,Client
from menuApp.serializers import CarteDuJourSerializer,PlatSerializer,LivreurSerializer,CommandeSerializer,DesertSerializer,PersonneSerializer,ClientSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def PlatApi(request,id=0):
    if request.method=='GET':
        plat = Plat.objects.all()
        Plat_serializer=PlatSerializer(plat,many=True)
        return JsonResponse(Plat_serializer.data,safe=False)
    elif request.method=='POST':
        Plat_data=JSONParser().parse(request)
        Plat_serializer=PlatSerializer(data=Plat_data)
        if Plat_serializer.is_valid():
            Plat_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Plat_data=JSONParser().parse(request)
        plat=Plat.objects.get(PlatId=Plat_data['PlatId'])
        Plat_serializer=PlatSerializer(plat,data=Plat_data)
        if Plat_serializer.is_valid():
            Plat_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        plat=Plat.objects.get(PlatId=id)
        Plat.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def CarteDuJourApi(request,id=0):
    if request.method=='GET':
        carteDuJour = CarteDuJour.objects.all()
        carteDuJour_serializer=CarteDuJourSerializer(carteDuJour,many=True)
        return JsonResponse(carteDuJour_serializer.data,safe=False)
    elif request.method=='POST':
        CarteDuJour_serializer=JSONParser().parse(request)
        CarteDuJour_serializer=CarteDuJourSerializer(data=CarteDuJour_data)
        if CarteDuJour_serializer.is_valid():
            CarteDuJour_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        CarteDuJour_data=JSONParser().parse(request)
        carteDuJour=CarteDuJour.objects.get(CarteDuJourId=CarteDuJour_data['CarteDuJourId'])
        CarteDuJour_serializer=CarteDuJourSerializer(carteDuJour,data=CarteDuJour_data)
        if CarteDuJour_serializer.is_valid():
            CarteDuJour_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        carteDuJour=CarteDuJour.objects.get(CarteDuJourId=id)
        CarteDuJour.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def DesertApi(request,id=0):
    if request.method=='GET':
        desert = Desert.objects.all()
        desert_serializer=DesertSerializer(desert,many=True)
        return JsonResponse(desert_serializer.data,safe=False)
    elif request.method=='POST':
        desert_data=JSONParser().parse(request)
        desert_serializer=DesertSerializer(data=desert_data)
        if desert_serializer.is_valid():
            desert_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        desert_data=JSONParser().parse(request)
        desert=Desert.objects.get(DesertId=desert_data['DesertId'])
        desert_serializer=DesertSerializer(desert,data=desert_data)
        if desert_serializer.is_valid():
            desert_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        desert=Livreur.objects.get(DesertId=id)
        desert.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def livreurApi(request,id=0):
    if request.method=='GET':
        livreur = Livreur.objects.all()
        livreur=LivreurSerializer(livreur,many=True)
        return JsonResponse(livreur.data,safe=False)
    elif request.method=='POST':
        livreur_data=JSONParser().parse(request)
        livreur_serializer=LivreurSerializer(data=livreur_data)
        if livreur_serializer.is_valid():
            livreur_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        livreur_data=JSONParser().parse(request)
        livreur=Livreur.objects.get(LivreurId=livreur_data['LivreurId'])
        livreur_serializer=LivreurSerializer(livreur,data=livreur_data)
        if livreur_serializer.is_valid():
            livreur_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        livreur=Livreur.objects.get(LivreurId=id)
        livreur.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def CommandeApi(request,id=0):
    if request.method=='GET':
        commande = Commande.objects.all()
        commande=CommandeSerializer(commande,many=True)
        return JsonResponse(commande.data,safe=False)
    elif request.method=='POST':
        commande_data=JSONParser().parse(request)
        commande_serializer=CommandeSerializer(data=commande_data)
        if commande_serializer.is_valid():
            commande_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        commande_data=JSONParser().parse(request)
        commande=Commande.objects.get(CommandeId=commande_data['CommandeId'])
        commande_serializer=CommandeSerializer(commande,data=commande_data)
        if commande_serializer.is_valid():
            commande_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        commande=Commande.objects.get(CommandeId=id)
        commande.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def PersonneApi(request,id=0):
    if request.method=='GET':
        personne = Personne.objects.all()
        personne=PersonneSerializer(personne,many=True)
        return JsonResponse(personne.data,safe=False)
    elif request.method=='POST':
        personne_data=JSONParser().parse(request)
        personne_serializer=PersonneSerializer(data=personne_data)
        if personne_serializer.is_valid():
            personne_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        personne_data=JSONParser().parse(request)
        personne=Personne.objects.get(PersonneId=personne_data['PersonneId'])
        personne_serializer=PersonneSerializer(personne,data=personne_data)
        if personne_serializer.is_valid():
            personne_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        personne=Personne.objects.get(PersonneId=id)
        personne.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def ClientApi(request,id=0):
    if request.method=='GET':
        client = Client.objects.all()
        client=ClientSerializer(client,many=True)
        return JsonResponse(client.data,safe=False)
    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        client_serializer=ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        client_data=JSONParser().parse(request)
        client=Client.objects.get(ClientId=client_data['ClientId'])
        client_serializer=PersonneSerializer( client,data= client_data)
        if  client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        client=Client.objects.get(ClientId=id)
        client.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)