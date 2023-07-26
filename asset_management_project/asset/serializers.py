from rest_framework import serializers
from .models import Station, Department, Section, User, Asset, Ticket, DeployedAsset


class StationSerializer(serializers.Serializer):
    class Meta:
        model = Station
        fields = ['name']


class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = ['name']


class SectionSerializer(serializers.Serializer):
    class Meta:
        model = Section
        fields = ['name', 'station']


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['personal_number', 'domain', 'name', 'station', 'section', 'role']


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        # fields = ['serial_number', 'asset_type', 'model_type', 'model_number', 'mac_address', 'os', 'wake_on_lan',
        #           'kav', 'status', 'location']
        fields = '__all__'


class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = ['ticket_number', 'ict_officer']


class DeployedAssetSerializer(serializers.Serializer):
    class Meta:
        model = DeployedAsset
        fields = ['asset', 'workticket', 'previous_owner', 'current_owner', 'previous_location', 'current_location',
                  'movement_form', 'movement_type']



