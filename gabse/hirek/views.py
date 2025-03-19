from django.shortcuts import render

# Create your views here.
def fooldal(request):
    return render(request, "hirek/index.html")

def edzok(request):
    return render(request, "hirek/edzok.html")

def csapataink(request):
    return render(request, "hirek/csapatok.html")


def u19(request):
    return render(request, "hirek/u19.html")

def u17(request):
    return render(request, "hirek/u17.html")

def u16(request):
    return render(request, "hirek/u16.html")

def u15(request):
    return render(request, "hirek/u15.html")

def u11(request):
    return render(request, "hirek/u11.html")

def felnott(request):
    return render(request, "hirek/felnott.html")

def oldboys(request):
    return render(request, "hirek/oldboys.html")

def oregfiuk(request):
    return render(request, "hirek/oregfiuk.html")
