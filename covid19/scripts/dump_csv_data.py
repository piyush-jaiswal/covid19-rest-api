import csv
import datetime

from covid19.models import Covid19India, CovidVaccineStatewise, StateWiseTestingDetails


def dump_covid_19_india():
    with open('C:\mystuff\homelane\Covid1929cc1f3\covid_19_india.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            date = row[1]
            time = row[2]
            state = row[3]

            try:
                indian_national = int(row[4])
            except ValueError:
                indian_national = None

            try:
                foreign_national = int(row[5])
            except ValueError:
                foreign_national = None

            try:
                cured = int(row[6])
            except ValueError:
                cured = None

            try:
                deaths = int(row[7])
            except ValueError:
                deaths = None

            try:
                confirmed = int(row[8])
            except ValueError:
                confirmed = None

            covid_row = Covid19India.objects.create(date=date, time=time, state_union_territory=state, confirmed_indian_national=indian_national, confirmed_foreign_national=foreign_national, cured=cured, deaths=deaths, confirmed=confirmed)
            print(covid_row.id)


def dump_covid_vaccine_statewise():
    with open("C:\mystuff\homelane\Covid1929cc1f3\covid_vaccine_statewise.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            updated_on = datetime.datetime.strptime(row[0], "%d/%m/%Y")
            state = row[1]

            try:
                total_doses_administered = int(float(row[2]))
            except ValueError:
                total_doses_administered = None

            try:
                total_sessions_conducted = int(float(row[3]))
            except ValueError:
                total_sessions_conducted = None

            try:
                total_sites = int(float(row[4]))
            except ValueError:
                total_sites = None

            try:
                first_dose_administered = int(float(row[5]))
            except ValueError:
                first_dose_administered = None

            try:
                second_dose_administered = int(float(row[6]))
            except ValueError:
                second_dose_administered = None

            try:
                male_vaccinated = int(float(row[7]))
            except ValueError:
                male_vaccinated = None

            try:
                female_vaccinated = int(float(row[8]))
            except ValueError:
                female_vaccinated = None

            try:
                transgender_vaccinated = int(float(row[9]))
            except ValueError:
                transgender_vaccinated = None

            try:
                total_covaxin_administered = int(float(row[10]))
            except ValueError:
                total_covaxin_administered = None

            try:
                total_coviShield_administered = int(float(row[11]))
            except ValueError:
                total_coviShield_administered = None

            try:
                total_sputnik5_administered = int(float(row[12]))
            except ValueError:
                total_sputnik5_administered = None

            try:
                aefi = int(float(row[13]))
            except ValueError:
                aefi = None

            try:
                age_18_45 = int(float(row[14]))
            except ValueError:
                age_18_45 = None

            try:
                age_45_60 = int(float(row[15]))
            except ValueError:
                age_45_60 = None

            try:
                age_60_plus = int(float(row[16]))
            except ValueError:
                age_60_plus = None

            try:
                total_individuals_vaccinated = int(float(row[17]))
            except ValueError:
                total_individuals_vaccinated = None

            row2 = CovidVaccineStatewise.objects.create(
                updated_on=updated_on,
                state=state,
                total_doses_administered=total_doses_administered,
                total_sessions_conducted=total_sessions_conducted,
                total_sites=total_sites,
                first_dose_administered=first_dose_administered,
                second_dose_administered=second_dose_administered,
                male_vaccinated=male_vaccinated,
                female_vaccinated=female_vaccinated,
                transgender_vaccinated=transgender_vaccinated,
                total_covaxin_administered=total_covaxin_administered,
                total_coviShield_administered=total_coviShield_administered,
                total_sputnik5_administered=total_sputnik5_administered,
                aefi=aefi,
                age_18_45=age_18_45,
                age_45_60=age_45_60,
                age_60_plus=age_60_plus,
                total_individuals_vaccinated=total_individuals_vaccinated,
            )
            print(row2.id)


def dump_statewise_testing_details():
    with open("C:\mystuff\homelane\Covid1929cc1f3\StatewiseTestingDetails.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            date = row[0]
            state = row[1]

            try:
                total_samples = int(float(row[2]))
            except ValueError:
                total_samples = None

            try:
                negative = int(float(row[3]))
            except ValueError:
                negative = None

            try:
                positive = int(float(row[4]))
            except ValueError:
                positive = None

            row2 = StateWiseTestingDetails.objects.create(
                date=date,
                state=state,
                total_samples=total_samples,
                negative=negative,
                positive=positive,
            )
            print(row2.id)


def run():
    dump_covid_19_india()
    print("------------------------------------------------------------------------------------------")
    dump_covid_vaccine_statewise()
    print("------------------------------------------------------------------------------------------")
    dump_statewise_testing_details()
    print("------------------------------------------------------------------------------------------")
