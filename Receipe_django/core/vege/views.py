from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def receipe(request):
        if request.method == "POST":
            data = request.POST

            receipe_image = request.FILES.get('receipe_image')
            receipe_name = data.get("receipe_name")
            receipe_desc = data.get('receipe_desc')



            Receipe.objects.create(
                receipe_name = receipe_name,
                receipe_desc = receipe_desc,
                receipe_image = receipe_image
            )

            return redirect('/receipe/')
        queryset = Receipe.objects.all()
        context = {'receipe' : queryset}
        return render(request,'receipe.html',context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')

