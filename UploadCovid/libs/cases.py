
from .reader import get_csv_reader
from .countries import countries

github_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

def get_covid_cases(date):
    csv_url = github_url + date +".csv"
    reader = get_csv_reader(csv_url)
    covid_cases=[]
    for row in reader:       
        if row[3] in countries:
            covid_cases.append(
                {
                "Country": row[3],
                "Confirmed": row[7],
                "Deaths": row[8],
                "Recovered": row[9],
                "Active": row[10]
                }
            )
    return covid_cases


        