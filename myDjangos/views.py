from django.shortcuts import render
from .models import Medicine, MedicineDocument
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .medicineDocManage import MedicineDocForm



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

