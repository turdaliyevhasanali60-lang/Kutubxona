from django.contrib import admin
from django.urls import path

from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', index),

    path('talabalar/', talabalar_view),
    path('talabalar/<int:talaba_id>/', talaba_retrieve_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('talabalar/<int:talaba_id>/delete/confirm/', talaba_delete_confirm_view),

    path('mualliflar/', mualliflar_view),
    path('mualliflar/<int:muallif_id>/delete/', muallif_delete_view),
    path('mualliflar/<int:muallif_id>/', muallif_retrieve_view),

    path('kitoblar/', kitoblar_view),
    path('kitoblar/<int:kitob_id>/', kitob_retrieve_view),
    path('kitoblar/<int:kitob_id>/delete/', kitob_delete_view),

    path('recordlar/', record_view),
    path('recordlar/<int:record_id>/', record_retrieve_view),
    path('recordlar/<int:record_id>/delete/', record_delete_view),


    path('tirik/', tirik_mualliflar_view),

    path('eng_3/', eng_3_kitob_view),

    path('eng_3_muallif/', eng_muallif_view),

    path('latest-records/', latest_records_view),

    path('books/', booksOftirik),

    path('badiiykitoblar/', badiybooks_view),

    path('oldestmualliflar/', oldestmualliflar_view),

    path('muallif3/', kitob3_mualliflar_view),

    path('bTalabaR/', bitiruvchiTalabarR_view),

    path('kutubxonachilar/', kutubxonachilar_view, name='kutubxonachilar'),
    path('kutubxonachi/', kutubxonachilar_view),

]