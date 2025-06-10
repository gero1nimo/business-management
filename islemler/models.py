from django.db import models

# Create your models here.

class Transaction(models.Model):
    islem_turu_secenekleri = (
        ('gelir', 'Gelir'),
        ('gider', 'Gider'),
    )
    islem_id = models.AutoField(primary_key=True, verbose_name="İşlem ID")
    islem_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="İşlem Tarihi")
    islem_turu = models.CharField(max_length=10, choices=islem_turu_secenekleri, verbose_name="İşlem Türü")
    islem_miktari = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="İşlem Miktarı")
    yapan_kisi = models.CharField(max_length=100, blank=False, null=False, verbose_name="Yapan Kişi")
    aciklama = models.TextField(blank=False, null=False, verbose_name="Açıklama")
    class Meta:
        verbose_name = "İşlem"
        verbose_name_plural = "İşlemler"
        ordering = ['-islem_tarihi']

    def __str__(self):
        return f"{self.aciklama} - {self.islem_turu} - {self.islem_miktari} ({self.islem_tarihi})"
    

    def create_transaction(self, islem_turu, islem_miktari, yapan_kisi, aciklama):
        self.islem_turu = islem_turu
        self.islem_miktari = islem_miktari
        self.yapan_kisi = yapan_kisi
        self.aciklama = aciklama
        self.save()
    
    def update_transaction(self, islem_id, islem_turu=None, islem_miktari=None, yapan_kisi=None, aciklama=None):
        transaction = Transaction.objects.get(islem_id=islem_id)
        if islem_turu:
            transaction.islem_turu = islem_turu
        if islem_miktari:
            transaction.islem_miktari = islem_miktari
        if yapan_kisi:
            transaction.yapan_kisi = yapan_kisi
        if aciklama:
            transaction.aciklama = aciklama
        transaction.save()  

    def delete_transaction(self, islem_id):
        transaction = Transaction.objects.get(islem_id=islem_id)
        transaction.delete()