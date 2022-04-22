from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=7, blank=True)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField(default=False)
    kitoblar_soni = models.PositiveSmallIntegerField(blank=True)
    yosh = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    JANR = (
        ("1", "Badiiy"),
        ("2", "Ilmiy"),
        ("3", "Hujjatli"),
        ("4", "Detektiv"),
        ("5", "Fantastik")
    )
    nom = models.CharField(max_length=50)
    sana = models.DateField(blank=True)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=15, choices=JANR)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE, related_name="m_kitoblari")
    def __str__(self):
        return self.nom

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    qaytardi = models.CharField(max_length=5,blank=True, default="Yo'q")
    qaytarish_sana = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"{self.kitob} ({self.student})"


