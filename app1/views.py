from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def salomlash(request):
    return render(request, "salomlash.html", {"ism":"Akmal"})

def man(request):
    return HttpResponse("Ismim Abdulhamid, Backend dasturchiman")

def loyiha(request):
    return HttpResponse("Bu loyiha kutubxona tizimini boshqarish uchun xizmat qiladi")

def asosiy(request):
    return render(request, "asosiy.html")

def kitoblar(request):
    if request.method == 'POST':
        m = request.POST.get("m")
        muallif = Muallif.objects.get(id=m)
        Kitob.objects.create(
            nom=request.POST.get("n"),
            sana=request.POST.get("s"),
            sahifa=request.POST.get("sahifa"),
            janr=request.POST.get("j"),
            muallif=muallif,
        )
        return redirect("/kitoblar/")
    soz = request.GET.get("qidirish")
    m = Muallif.objects.all()
    if soz == None:
        hammasi = Kitob.objects.all().order_by("nom")
    else:
        hammasi = Kitob.objects.filter(nom=soz)
    return render(request, "books.html", {"kitoblar":hammasi,"avtorlar":m})

def mualliflar(request):
    if request.method == 'POST':
        if request.POST.get("t") == "False":
            natija = False
        else:
            natija = True
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            tirik=natija,
            yosh=request.POST.get("y"),
            kitoblar_soni=request.POST.get("k_s")
        )
        return redirect("/mualliflar/")
    m = Muallif.objects.all().order_by("ism")
    return render(request, "muallif.html", {"avtorlar":m})

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/kitoblar/")

def records(request):
    if request.method == 'POST':
        st = Student.objects.get(id=request.POST.get("s"))
        kt = Kitob.objects.get(id=request.POST.get("k"))
        if st.kitob_soni == 3:
            return HttpResponse("<h1>Biz sizga kitob berolmaymiz, oldingilarini qaytaring!</h1>")
        Record.objects.create(
            student=st,
            kitob = kt,
            sana = request.POST.get("sana")
        )
        st.kitob_soni = st.kitob_soni + 1
        st.save()
        return redirect("/record/")
    s = Student.objects.all()
    k = Kitob.objects.all()
    r = Record.objects.all()
    return render(request, "record.html", {"recordlar":r, "books":k,"students":s})

def muallif_edit(request, pk):
    if request.method == 'POST':
        m1 = Muallif.objects.get(id=pk)
        m1.ism=request.POST.get("ismi")
        m1.yosh=request.POST.get("y")
        m1.kitoblar_soni=request.POST.get("k_s")
        m1.save()
        return redirect("/mualliflar/")
    m = Muallif.objects.get(id=pk)
    return render(request, "muallif-edit.html", {"muallif":m})


def kitob_edit(request, a):
    if request.method== 'POST':
        k1 = Kitob.objects.get(id=a)
        k1.nom=request.POST.get("n")
        k1.sahifa=request.POST.get("s")
        k1.janr=request.POST.get("j")
        o=Muallif.objects.get(id=request.POST.get("muallif"))
        k1.muallif=o
        k1.save()
        return redirect("/kitoblar/")
    ka=Kitob.objects.get(id=a)
    m=Muallif.objects.all()
    return render(request,  "kitob_edit.html", {"kitob":ka,"muallif":m})

def record_edit(request, pk):
    if request.method == 'POST':
        r1 = Record.objects.get(id=pk)
        r1.qaytardi = request.POST.get("q")
        try:
            r1.qaytarish_sana = request.POST.get("sana2")
            r1.save()
            st = r1.student
            st.kitob_soni -= 1
            st.save()
        except:
            pass
        return redirect("/record/")
    r = Record.objects.get(id=pk)
    return render(request, "record-edit.html", {"rec":r})


