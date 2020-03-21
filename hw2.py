from typing import List
import pandas as pd
import datetime
import os

# confirmed cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
dfC = pd.read_csv(url, error_bad_lines=False)

# deaths
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
dfD = pd.read_csv(url, error_bad_lines=False)

# recovered cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
dfR = pd.read_csv(url, error_bad_lines=False)


# Helper function (strftime not cross platform) ???
def format_date(date: datetime.date):
    if os.name == "nt":
        return date.strftime('%#m/%#d/%y')
    else:
        return date.strftime('%-m/%-d/%y')


def countries_with_no_deaths_count(date: datetime.date) -> int:
  i = 0
  d = format_date(date)
  for w in dfC.index:
    if dfC.at[w,d] !=0 and dfD.at[w,d] == 0:
      i=i+1
  return i

def more_cured_than_deaths_indices(date: datetime.date) -> List[int]:
  i = []
  d = format_date(date)
  for w in dfC.index:
    if dfR.at[w,d] > dfD.at[w,d]:
      i.append(w)
  return i
