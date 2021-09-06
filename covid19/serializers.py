from rest_framework import serializers
from covid19.models import Covid19India, CovidVaccineStatewise, StateWiseTestingDetails


class Covid19IndiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19India
        fields = ('date',
                  'time',
                  'state_union_territory',
                  'confirmed_indian_national',
                  'confirmed_foreign_national',
                  'cured',
                  'deaths',
                  'confirmed')


class CovidVaccineStatewiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidVaccineStatewise
        fields = ('updated_on',
                  'state',
                  'total_doses_administered',
                  'total_sessions_conducted',
                  'total_sites',
                  'first_dose_administered',
                  'second_dose_administered',
                  'male_vaccinated',
                  'female_vaccinated',
                  'transgender_vaccinated',
                  'total_covaxin_administered',
                  'total_coviShield_administered',
                  'total_sputnik5_administered',
                  'aefi',
                  'age_18_45',
                  'age_45_60',
                  'age_60_plus',
                  'total_individuals_vaccinated')


class StateWiseTestingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateWiseTestingDetails
        fields = ('date',
                  'state',
                  'total_samples',
                  'negative',
                  'positive')


class GetDateInfoRequestSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)


class GetStateInfoRequestSerializer(serializers.Serializer):
    state = serializers.CharField(required=True)


class PinpointStateRequestSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    state = serializers.CharField(required=True)
