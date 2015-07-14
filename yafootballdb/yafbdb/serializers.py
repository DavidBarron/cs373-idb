from yafbdb.models import Division, Team, Player
from rest_framework import serializers


class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Division
        fields = ('division', 'dimage', 'conference', 'cimage', 'founded', 'rchamp', 'mchamps', 'cnum')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('team', 'division', 'timage', 'state', 'city', 'stadium', 'simage', 'coach', 'established', 'cchamps', 'schamps')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'team', 'number', 'position', 'height', 'weight', 'age', 'experience', 'college', 'pimage')