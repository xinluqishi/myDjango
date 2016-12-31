from django.db import models

'''To be the medical document which including many medicine objects'''


class MedicineDocument(models.Model):

    medicine_document_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回model的字符串表达"""
        return self.medicine_document_name


'''To be the medicine object'''


class Medicine(models.Model):

    medicine_document = models.ForeignKey(MedicineDocument)
    medicine_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'medicines'

    def __str__(self):
        return self.medicine_name[:50] + "..."




