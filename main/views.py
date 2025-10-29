from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import *

def test_view(request):
    return HttpResponse(
        """
        <h1 style="color: teal;" >Bosh Sahifa </h1>
        <hr>
        <p> Bugun Djanda</p>
        """
    )

def index(request):
    context = {
        "now": datetime.datetime.now(),
    }
    return render(request, 'index.html', context)

def talabalar_view(request):
    talabalar = Talaba.objects.all()

    search = request.GET.get('search')
    if search:
        talabalar = talabalar.filter(ism__contains=search)

    order = request.GET.get('order')
    if order:
        talabalar = talabalar.order_by(order)

    kurs = request.GET.get('kurs')
    if kurs and int(kurs) != 0:
        talabalar = talabalar.filter(kurs=kurs)


    context = {
        "talabalar": talabalar,
        "search": search,
        "order": order,
        "kurs": kurs,
    }
    return render(request, 'talabalar.html', context)

def talaba_retrieve_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba": talaba,
    }
    return render(request, 'talaba-retrieve_view.html', context)

def talaba_delete_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('/talabalar/')

def talaba_delete_confirm_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba": talaba,
    }
    return render(request, 'talaba-delete_confirm_view.html', context)


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    order = request.GET.get('order')
    if order:
        mualliflar = mualliflar.order_by(order)

    context = {
        "mualliflar": mualliflar,
        "order": order,
    }
    return render(request, 'mualliflar.html', context)

def muallif_delete_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect('/mualliflar/')

def muallif_retrieve_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        "muallif": muallif,
    }
    return render(request, 'muallif-retrieve_view.html', context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    search = request.GET.get('search')



    if search:
        kitoblar = kitoblar.filter(nom__contains=search)

    context = {
        "kitoblar": kitoblar,
        "search": search,
    }
    return render(request, 'kitoblar.html', context)

def kitob_retrieve_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        "kitob": kitob,
    }
    return render(request, 'kitob_retrieve_view.html', context)

def kitob_delete_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect('/kitoblar/')

def record_view(request):
    recordlar = Record.objects.all()
    order = request.GET.get('order')
    if order:
        recordlar = recordlar.order_by(order)

    context = {
        "recordlar": recordlar,
        "order": order,
    }
    return render(request, 'recordlar.html', context)

def record_delete_view(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('/records/')

def record_retrieve_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        "record": record,
    }
    return render(request, 'record-retrieve_view.html', context)

def tirik_mualliflar_view(request):
    tirik_mualliflar = Muallif.objects.filter(tirik=True)
    context = {
        "tirik_mualliflar": tirik_mualliflar,
    }
    return render(request, 'tirik_mualliflar.html', context)

def eng_3_kitob_view(request):
    eng_3_kitob = Kitob.objects.order_by("sahifa")[:3]
    context = {
        "eng_3_kitob": eng_3_kitob,
    }
    return render(request, 'eng_3_kitob.html', context)

def eng_muallif_view(request):
    eng_muallif = Muallif.objects.order_by("kitob_soni")[:3]
    context = {
        "eng_muallif": eng_muallif,
    }
    return render(request, 'eng_muallif.html', context)

def latest_records_view(request):
    latest_records = Record.objects.order_by("olingan_sana")[:3]
    context = {
        "latest_records": latest_records,
    }
    return render(request, 'latest_records.html', context)

def booksOftirik(request):
    booksOfTirikM = Kitob.objects.filter(muallif__tirik=True)
    context = {
        "booksOfTirikM": booksOfTirikM,
    }
    return render(request, 'books-of-tirik.html', context)

def badiybooks_view(request):
    badiiykitoblar = Kitob.objects.filter(janr="badiiy")
    context = {
        "badiiykitoblar": badiiykitoblar,
    }
    return render(request, 'badiiykitoblar.html', context)

def oldestmualliflar_view(request):
    oldestmualliflar =Muallif.objects.order_by("tugilgan_sana")[3:]
    context = {'oldestmualliflar': oldestmualliflar}
    return render(request, 'oldestmualliflar.html', context)

def kitob3_mualliflar_view(request):
    kitob3_mualliflar = Muallif.objects.filter(kitob_soni__lt=3)
    context = {
        "kitob3_mualliflar": kitob3_mualliflar,
    }
    return render(request, 'kitob3_mualliflar.html', context)

def bitiruvchiTalabarR_view(request):
    bitiruvchiTalabarR = Record.objects.filter(talaba__kurs=4)
    context = {
        "bitiruvchiTalabarR": bitiruvchiTalabarR,
    }
    return render(request, 'bitiruvchiTalabarR.html', context)

