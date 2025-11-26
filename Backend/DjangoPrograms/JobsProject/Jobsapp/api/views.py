from rest_framework import viewsets
from Jobsapp.api.serializers import HydJobsSerializer
from Jobsapp.models import Hydjobs
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    queryset = Hydjobs.objects.all()
    serializer_class = HydJobsSerializer
