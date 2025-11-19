from rest_framework import serializers
from testapp.models import Employee

def multiples_of_1000(value):
                    print('Validation by validator attribute')
                    if value%1000 != 0:
                        raise serializers.ValidationError('Employee sal should be multiples of 1000')

# class EmployeeSerializer(serializers.Serializer):
#                   eno = serializers.IntegerField()
#                   ename = serializers.CharField(max_length=10)
#                   esal = serializers.FloatField(validators=[multiples_of_1000])
#                   eaddr = serializers.CharField(max_length=30)



#                 #   def create(self,validated_data):
#                 #           return(Employee.objects.create(**validated_data))
                  
#                   def validate_esal(self,value):
#                       print("filed level")
#                       if value < 5000:
#                        raise serializers.ValidationError('Employee salary should be minimum 5000')
#                       return value
                  
#                   def validate(self,data):
#                       ename = data.get('ename')
#                       esal = data.get('esal')
#                       if ename.lower() == 'sunny':
#                           print("object level")
#                           if esal < 50000:
#                               raise serializers.ValidationError('Sunny sal should be minimum 50000')
#                       return data

	               
#                   def update(self, instance, validated_data):
#                         instance.eno = validated_data.get('eno',instance.eno)
#                         instance.ename = validated_data.get('ename', instance.ename)
#                         instance.esal = validated_data.get('esal', instance.esal)
#                         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#                         instance.save()
#                         return instance




class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000])
    class Meta:
        model = Employee
        fields = '__all__'