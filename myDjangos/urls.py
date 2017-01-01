"""My Djangos Urls"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Main Page
    url(r'^$', views.index, name='index'),

    # Show All Medicine Documents
    url(r'^medicineDocs/$', views.medicine_docs, name='medicineDocs'),

    # Medicine Document Detail Page
    url(r'^medicineDocs/(?P<medicinedoc_id>\d+)/$', views.medicine_doc_detail, name='medicineDocDetail'),
]