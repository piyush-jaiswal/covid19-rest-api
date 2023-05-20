# covid19-rest-api
RESTful HTTP API using `Django` and `Django REST framework` to fetch details of the Covid19 cases registered and the vaccinations administered in India.

Requests sent to the server are validated, including the data types in which the request data is expected with support for custom types such as dates, sending the appropriate response 
in case validation fails. The details are then fetched from DB using `Django's ORM`, serialized and returned in a `JSON` response.

### Requirements
This project is written in `python3.7`
```bash
pip install -r requirements.txt
```


### Setup
Create DB tables and populate data.
```
python manage.py migrate
python manage.py runscript dump_csv_data.py
```
Currently, the DB is `sqlite`. To work with something else, specify details in the `DATABASES` variable in `data_service/settings.py`


### Usage

Start the server:

`python manage.py runserver` (Starts the server on 127.0.0.1:8000)

<br/>

### Endpoints

- [GET] `/covid19/get-date-info` - Fetches details for all States and Union Territories on a particular date
```
JSON:
{
  "date": "YYYY-MM-DD"
}
```
<br/>

- [GET] `/covid19/get-state-info` - Fetches details of a State or Union Territory for all dates present in the database
```
JSON:
{
  "state": "<any state or UT in India>"
}
```
<br/>

- [GET] `/covid19/pinpoint-state` - Fetches details of a State or Union Territory on a particular date
```
JSON:
{
  "date": "YYYY-MM-DD",
  "state": "<any state or UT in India>"
}
```

### Data
Present in `covid19/data:`

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
