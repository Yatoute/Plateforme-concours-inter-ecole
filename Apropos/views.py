from django.shortcuts import render, redirect
from home.models import Newsletter
def Apropos_view(request):

    return render(request,'Apropos/Apropos.html')