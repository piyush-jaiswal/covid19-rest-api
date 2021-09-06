from django.db import models


class Covid19India(models.Model):
    date = models.DateField()
    time = models.TimeField()
    state_union_territory = models.CharField(max_length=100)
    confirmed_indian_national = models.IntegerField(null=True)
    confirmed_foreign_national = models.IntegerField(null=True)
    cured = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    confirmed = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.date}, {self.time}, {self.state_union_territory}, {self.confirmed_indian_national}, " \
              f"{self.confirmed_foreign_national}, {self.cured}, {self.deaths}, {self.confirmed}"


class CovidVaccineStatewise(models.Model):
    updated_on = models.DateField()
    state = models.CharField(max_length=100)
    total_doses_administered = models.IntegerField(null=True)
    total_sessions_conducted = models.IntegerField(null=True)
    total_sites = models.IntegerField(null=True)
    first_dose_administered = models.IntegerField(null=True)
    second_dose_administered = models.IntegerField(null=True)
    male_vaccinated = models.IntegerField(null=True)
    female_vaccinated = models.IntegerField(null=True)
    transgender_vaccinated = models.IntegerField(null=True)
    total_covaxin_administered = models.IntegerField(null=True)
    total_coviShield_administered = models.IntegerField(null=True)
    total_sputnik5_administered = models.IntegerField(null=True)
    aefi = models.IntegerField(null=True)
    age_18_45 = models.IntegerField(null=True)
    age_45_60 = models.IntegerField(null=True)
    age_60_plus = models.IntegerField(null=True)
    total_individuals_vaccinated = models.IntegerField(null=True)


class StateWiseTestingDetails(models.Model):
    date = models.DateField()
    state = models.CharField(max_length=100)
    total_samples = models.IntegerField(null=True)
    negative = models.IntegerField(null=True)
    positive = models.IntegerField(null=True)


