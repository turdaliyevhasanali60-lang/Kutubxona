from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import *
from .forms import *

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
    talaba_form = TalabaForm()
    # if request.method == "POST":
    #     Talaba.objects.create(
    #         ism = request.POST.get("ism"),
    #         guruh = request.POST.get("guruh"),
    #         kurs = request.POST.get("kurs"),
    #         kitob_soni = request.POST.get("kitob_soni") if request.POST.get("kitob_soni") else 0,
    #     )
    #     return redirect('/talabalar/')

    if request.method == "POST":
        form_data = TalabaForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            Talaba.objects.create(
                ism = data['ism'],
                guruh = data['guruh'],
                kurs = data['kurs'],
                kitob_soni = data['kitob_soni'],
            )
        return redirect('/talabalar/')


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
        "form": talaba_form,

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
    return redirect('talabalar')

def talaba_update_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    if request.method == "POST":
        Talaba.objects.filter(id=talaba_id).update(
            ism = request.POST.get("ism"),
            guruh = request.POST.get("guruh"),
            kurs = request.POST.get("kurs") if request.POST.get("kurs") else 0,
            kitob_soni = request.POST.get("kitob_soni") if request.POST.get("kitob_soni") else 0,
        )
        return redirect('/talabalar/', talaba_id)
    context = {
        "talaba": talaba,
    }
    return render(request, 'talaba-update_view.html', context)

def talaba_delete_confirm_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba": talaba,
    }
    return render(request, 'talaba-delete_confirm_view.html', context)


def mualliflar_view(request):
    # if request.method == "POST":
    #     Muallif.objects.create(
    #         ism = request.POST.get("ism"),
    #         jins = request.POST.get("jins"),
    #         tugilgan_sana = request.POST.get("tugilgan_sana"),
    #         kitob_soni = request.POST.get("kitob_soni"),
    #         tirik=True if request.POST.get("tirik") == "on" else False,
    #     )
    form = MuallifForm()
    mualliflar = Muallif.objects.all()

    if request.method == "POST":
        form_data = MuallifForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        return redirect('/mualliflar/')

    order = request.GET.get('order')
    if order:
        mualliflar = mualliflar.order_by(order)

    context = {
        "mualliflar": mualliflar,
        "order": order,
        "form": form,
    }
    return render(request, 'mualliflar.html', context)

def muallif_update_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    if request.method == "POST":
        Muallif.objects.filter(id=muallif_id).update(
            ism = request.POST.get("ism"),
            jins = request.POST.get("jins"),
            tugilgan_sana = request.POST.get("tugilgan_sana") if request.POST.get("tugilgan_sana") else None,
            kitob_soni = request.POST.get("kitob_soni") if request.POST.get("kitob_soni") else 0,
            tirik = True if request.POST.get("tirik") == "on" else False,
        )

        return redirect('/mualliflar/')
    context = {
        "muallif": muallif,
    }
    return render(request, 'muallif-update_view.html', context)

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
    # if request.method == "POST":
    #     Kitob.objects.create(
    #         nom=request.POST.get("nom"),
    #         janr=request.POST.get("janr"),
    #         sahifa=request.POST.get("sahifa"),
    #         muallif=get_object_or_404(Muallif, id=request.POST.get("muallif_id")),
    #     )
    kitoblar = Kitob.objects.all()
    search = request.GET.get('search')
    mualliflar = Muallif.objects.all()
    form = KitobForm()

    if request.method == "POST":
        form_data = KitobForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        return redirect('kitoblar')



    if search:
        kitoblar = kitoblar.filter(nom__contains=search)

    context = {
        "kitoblar": kitoblar,
        "search": search,
        "mualliflar": mualliflar,
        'form': form,
    }
    return render(request, 'kitoblar.html', context)

def kitob_update_view(request, kitob_id):
    mualliflar = Muallif.objects.all()
    kitob = Kitob.objects.get(id=kitob_id)
    if request.method == "POST":
        Kitob.objects.filter(id=kitob_id).update(
            nom = request.POST.get("nom"),
            janr = request.POST.get("janr"),
            sahifa = request.POST.get("sahifa"),
            muallif = request.POST.get("muallif"),
        )
        return redirect('/kitoblar/', kitob_id)

    context = {
        "kitob": kitob,
        "mualliflar": mualliflar,
    }
    return render(request, 'kitob_update_view.html', context)

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
    # if request.method == "POST":
    #     Record.objects.create(
    #         talaba=get_object_or_404(Talaba, id=request.POST.get("talaba_id")),
    #         kitob=get_object_or_404(Kitob, id=request.POST.get("kitob_id")),
    #         kutubxonachi=get_object_or_404(Kutubxonachi, id=request.POST.get("kutubxonachi_id")),
    #         olingan_sana=request.POST.get("olingan_sana"),
    #         qaytarish_sana=request.POST.get("qaytarish_sana"),
    #     )
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/recordlar/')

    recordlar = Record.objects.all()
    order = request.GET.get('order')
    if order:
        recordlar = recordlar.order_by(order)

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        "recordlar": recordlar,
        "order": order,
        "talabalar": talabalar,
        "kitoblar": kitoblar,
        "kutubxonachilar": kutubxonachilar,
        "form": form,
    }
    return render(request, 'recordlar.html', context)

def record_update_view(request, record_id):
    record = Record.objects.get(id=record_id)
    if request.method == "POST":
        Record.objects.filter(id=record_id).update(
            talaba=request.POST.get("talaba"),
            kitob=request.POST.get("kitob"),
            kutubxonachi=request.POST.get("kutubxonachi"),
            olingan_sana=request.POST.get("olingan_sana"),
            qaytarish_sana=request.POST.get("qaytarish_sana"),
        )
    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        "talabalar": talabalar,
        "kitoblar": kitoblar,
        "kutubxonachilar": kutubxonachilar,
        "record": record,
    }
    return render(request, 'record_update_view.html', context)

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


def kutubxonachilar_view(request):
    # if request.method == "POST":
    #     ism = request.POST.get("ism")
    #     ish_vaqti = request.POST.get("ish_vaqti")
    #     if ism and ish_vaqti:
    #         Kutubxonachi.objects.create(ism=ism, ish_vaqti=ish_vaqti)
    #         return redirect('/kutubxonachi/')
    kutubxonachilar = Kutubxonachi.objects.all()
    form = KutubxonachiForm()
    if request.method == "POST":
        form = KutubxonachiForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/kutubxonachilar/')
    working_hours_options = [
        "09:00-17:00",
        "10:00-18:00",
        "12:00-20:00"
    ]
    search = request.GET.get('search')
    if search:
        kutubxonachilar = kutubxonachilar.filter(ism__contains=search)
    context = {
        "kutubxonachilar": kutubxonachilar,
        "search": search,
        "working_hours_options": working_hours_options,
        "form": form,
    }
    return render(request, 'kutubxonachilar.html', context)

def kutubxonachi_update_view(request, kutubxonachi_id):
    kutubxonachi = Kutubxonachi.objects.get(id=kutubxonachi_id)
    kutubxonachilar = Kutubxonachi.objects.all()
    working_hours_options = [
        "09:00-17:00",
        "10:00-18:00",
        "12:00-20:00"
    ]
    if request.method == "POST":
        Kutubxonachi.objects.filter(id=kutubxonachi_id).update(
            ism=request.POST.get("ism"),
            ish_vaqti=request.POST.get("ish_vaqti"),
        )
        return redirect('kutubxonachilar')
    context = {
        "kutubxonachilar": kutubxonachilar,
        "kutubxonachi": kutubxonachi,
        "working_hours_options": working_hours_options,
    }
    return render(request, 'kutubxonachi-update_view.html', context)

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

