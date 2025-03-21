# covid19-rest-api
RESTful HTTP API using `Django` and `Django REST framework` to fetch details of the Covid19 cases registered and the vaccinations administered in India.

Requests sent to the server are validated, including the data types in which the request data is expected with support for custom types such as dates, sending the appropriate response in case validation fails. The details are then fetched from DB using `Django's ORM`, serialized and returned in a `JSON` response.

Deployed on PythonAnywhere: [piyushj.pythonanywhere.com](piyushj.pythonanywhere.com)

### Requirements
This project is written in `python3.7`
```bash
pip install -r requirements.txt
```


### Setup

Copy `.env.example` and rename to `.env`. Set the environment variables.

To generate sample keys for the `DJANGO_SECRET_KEY` environment variable, in a python shell run:
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()  # 'p#+mx&9ef4d1*#1u_aofw2-!zv06czc#t%2h@d6+2=-eze#u*^'
```

Create DB tables and populate data.
```bash
python manage.py migrate
python manage.py runscript dump_csv_data
```
Currently, the DB is `sqlite`. To work with something else, specify details in the `DATABASES` variable in `data_service/settings.py`


### Usage
Start the server:

`python manage.py runserver` (Starts the server on 127.0.0.1:8000)

<br/>

### Endpoints

- [GET] `/covid19/get-date-info?date=<YYYY-MM-DD>` - Fetches details for all States and Union Territories on a particular date. Ex: `date=2020-10-01`

<br/>

- [GET] `/covid19/get-state-info?state=<State/UT in India>` - Fetches details of a State or Union Territory for all dates present in the database. Ex: `state=Andhra Pradesh`


<br/>

- [GET] `/covid19/pinpoint-state?date=<YYYY-MM-DD>&state=<State/UT in India>` - Fetches details of a State or Union Territory on a particular date


### Data

State names are capitalized and space separated:
- Andhra Pradesh
- Maharashtra
- West Bengal
- Jammu and Kashmir
- Andaman and Nicobar Islands

<br>

Data present in `covid19/data`:

`covid_19_india.csv`
- Sno
- Date
- Time
- State/UnionTerritory
- ConfirmedIndianNational
- ConfirmedForeignNational
- Cured
- Deaths
- Confirmed [ConfirmedIndianNational + ConfirmedForeignNational]

<br/>

`covid_vaccine_statewise.csv`
- Updated On
- State
- Total Doses Administered
- Total Sessions Conducted
- Total Sites
- First Dose Administered
- Second Dose Administered
- Male(Individuals Vaccinated)
- Female(Individuals Vaccinated)
- Transgender(Individuals Vaccinated)
- Total Covaxin Administered
- Total CoviShield Administered
- Total Sputnik V Administered
- AEFI
- 18-45 years (Age)
- 45-60 years (Age)
- 60+ years (Age)
- Total Individuals Vaccinated

<br/>

`StatewiseTestingDetails.csv`
- Date
- State	
- TotalSamples	
- Negative	
- Positive
