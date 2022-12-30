from django.db import models

# Create your models here.
class WagonType(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class CargoType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class WagonAssembly(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class WagonComponent(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class WagonDefect(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class EmployeeName(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class WagonStatus(models.Model):
    name = models.BooleanField()
    def __str__(self):
        if(self.name):
            return "груженный"
        else:
            return "порожний" 

class ReportTable(models.Model):
    date = models.DateField()
    wagonType = models.ForeignKey(WagonType, on_delete = models.CASCADE, verbose_name='WagonType', related_name='table')
    wagonNum = models.CharField(max_length=8)
    wagonStatus = models.ForeignKey(WagonStatus, on_delete = models.CASCADE, verbose_name='WagonStatus', related_name='table')
    CargoType = models.ForeignKey(CargoType, on_delete = models.CASCADE, verbose_name='CargoType', related_name='table')
    wagonAssembly = models.ForeignKey(WagonAssembly, on_delete = models.CASCADE, verbose_name='WagonAssembly', related_name='table')
    WagonComponent = models.ForeignKey(WagonComponent, on_delete = models.CASCADE, verbose_name='WagonComponent', related_name='table')
    wagonDefect = models.ForeignKey(WagonDefect, on_delete = models.CASCADE, verbose_name='WagonDefect', related_name='table')
    wagonNumNewComponents = models.IntegerField()
    dateRepair = models.DateField(null=True)
    employeeName = models.ForeignKey(EmployeeName, on_delete = models.CASCADE, verbose_name='EmployeeName', related_name='table')
    note = models.CharField(max_length=50)
