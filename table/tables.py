import django_tables2 as tables
from .models import ReportTable

class PersonTable(tables.Table):
    class Meta:
        model = ReportTable
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )