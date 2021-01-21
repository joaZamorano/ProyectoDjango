from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'usuario/inicio.html', {})
def lista(request):
    return render(request, 'usuario/lista_persona.html', {})
    
#def acceso(request):
'''    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("Usted está logeado")
    else:
        return HttpResponse("Tu usuario o contraseña no son correctos")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("Sesión cerrada")'''
