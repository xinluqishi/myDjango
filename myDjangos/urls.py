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

    # Add a new object for medicine document
    url(r'^new_medicine_doc/$', views.new_medicine_doc, name='new_medicine_doc'),

    # Add a new medicine in the medicine document detail page
    url(r'^new_medicine/(?P<medicinedoc_id>\d+)/$', views.medicine_detail, name='medicineDetail'),

    # Edit a medicine record
    url(r'^edit_medicine/(?P<medicine_id>\d+)/$', views.edit_medicine, name='editMedicine'),
]