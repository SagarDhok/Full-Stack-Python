from rest_framework.serializers import ModelSerializer
from Jobsapp.models import Hydjobs
class HydJobsSerializer(ModelSerializer):
    class Meta:
        model = Hydjobs
        fields = '__all__'
