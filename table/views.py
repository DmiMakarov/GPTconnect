from django_tables2 import SingleTableView
from django.views.generic import ListView
from .models import ReportTable
#from .tables import ReportTableTable

class ReportListView(ListView):
    model = ReportTable
    #table_class = ReportTableTable
    template_name = 'table.html'
