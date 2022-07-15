from rest_framework import serializers

from ENCOST.models import Duration, Client, Equipment, Mode


class DurationSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    equipment = serializers.SerializerMethodField()
    mode = serializers.SerializerMethodField()

    @staticmethod
    def get_client(obj):
        return Client.objects.get(pk=obj.client_id).name

    @staticmethod
    def get_equipment(obj):
        return Equipment.objects.get(pk=obj.equipment_id).name

    @staticmethod
    def get_mode(obj):
        return Mode.objects.get(pk=obj.mode_id).name

    class Meta:
        model = Duration
        fields = '__all__'
