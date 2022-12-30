from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(WagonType) 
admin.site.register(CargoType)
admin.site.register(WagonAssembly)
admin.site.register(WagonComponent)
admin.site.register(WagonDefect)
admin.site.register(EmployeeName)
admin.site.register(ReportTable)
admin.site.register(WagonStatus)