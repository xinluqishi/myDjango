from django.shortcuts import render
from .models import Medicine, MedicineDocument
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .medicineDocManage import MedicineDocForm, MedicineForm
import logging


def index(request):
    return render(request, 'myDjangos/index.html')


def medicine_docs(request):
    medicineDocsList = MedicineDocument.objects.order_by('date_added')
    context = {'medicineDocsList': medicineDocsList}
    return render(request, 'myDjangos/medicine_docs.html', context)


def medicine_doc_detail(request, medicinedoc_id):
    medicineDocValue = MedicineDocument.objects.get(id=medicinedoc_id)
    medicinesList = medicineDocValue.medicine_set.order_by('-date_added')
    context = {'medicineDocValue': medicineDocValue, 'medicines': medicinesList}
    return render(request, 'myDjangos/medicine_doc_detail.html', context)


def new_medicine_doc(request):
    if request.method != 'POST':
        form = MedicineDocForm()
    else:
        form = MedicineDocForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myDjangos:medicineDocs'))

    context = {'form': form}
    return render(request, 'myDjangos/new_medicine_doc.html', context)


def medicine_detail(request, medicinedoc_id):
    logging.debug("medicinedoc_id is: " + medicinedoc_id)
    medicineDoc = MedicineDocument.objects.get(id=medicinedoc_id)

    if request.method != 'POST':
        form = MedicineForm()

    else:
        form = MedicineForm(request.POST)
        if form.is_valid():
            new_medicine = form.save(commit=False)
            new_medicine.medicine_document = medicineDoc
            new_medicine.save()
            return HttpResponseRedirect(reverse('myDjangos:medicineDocDetail', args=[medicinedoc_id]))

    context = {'medicineDoc': medicineDoc, 'form': form}
    return render(request, 'myDjangos/new_medicine.html', context)


def edit_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicineDocument = medicine.medicine_document

    if request.method != 'POST':
        form = MedicineForm(instance=medicine)
    else:
        form = MedicineForm(instance=medicine, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myDjangos:medicineDocDetail', args=[medicineDocument.id]))

    context = {'medicine': medicine, 'medicineDocument': medicineDocument, 'form': form}
    return render(request, 'myDjangos/edit_medicine.html', context)
