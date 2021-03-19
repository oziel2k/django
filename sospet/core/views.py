from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet


@login_required(login_url='/login/')
def pet_salvar(request):

    pet_id          = request.POST.get('petid')
    cidade          = request.POST.get('cidade')
    descricao       = request.POST.get('descricao')
    telefone        = request.POST.get('telefone')
    email           = request.POST.get('email')
    foto            = request.FILES.get('fotopet')
    usuario         = request.user

    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if usuario == pet.usuario:
            pet.cidade      = cidade
            pet.descricao   = descricao
            pet.telefone    = telefone
            pet.email       = email
            if foto:
                pet.foto = foto

            pet.save()

    else:
        pet = Pet.objects.create(
            cidade=cidade,        
            descricao=descricao,
            telefone=telefone,
            email=email,        
            usuario=usuario,
            foto=foto
            )

    
    
    url = "/pet/detail/{}".format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def pet_delete(request, id):
    pet = Pet.objects.get(id=id)
    
    if pet.usuario == request.user:
        pet.delete()
    return redirect('/pet/all')

@login_required(login_url='/login/')
def pet_new(request):

    pet_id = request.GET.get('id')

    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.usuario == request.user:
           return render(request,'registrar.html',{'pet':pet})    
    
    return render(request,'registrar.html')    

@login_required(login_url='/login/')
def pet_detail(request, id):
    pet = Pet.objects.get(id=id)
    return render(request,'pet.html', {'pet':pet})

@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True,usuario=request.user)
    return render(request,'list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(ativo=True)
    return render(request,'list.html', {'pet':pet})

@login_required(login_url='/login/')
def inicial(request):
    return render(request,'home.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')
    #return  render(request,'logout.html')

def login_user(request):
    return  render(request,'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Dados não conferem')
    
    return redirect('/login')




