from rest_framework import serializers
from iot.models import Datapoint

#
# class GoodsSerializer(serializers.Serializer):
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass
#
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)

class DatapointSerializer(serializers.ModelSerializer):
   class Meta:
       model = Datapoint
       fields = ('sensor', 'value', 'time')
