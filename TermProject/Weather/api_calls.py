import os 
import calendar
import requests

# Make a dict to hold the month number and the date of the last day
months = {}

for i in range(1,13):
    # Get last day of the month
    date = calendar.monthrange(2022, i)
    # Add the month and last day to the dict
    months[i] = date[1]
# Make sure it looks good
print(months)
start_date = ""
end_date = ""
# URL for making the API requests
#url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago%2CUnited%20States/{date_start}/{date_end}?unitGroup=metric&key=2QHAY33FP8938JAMTYLD5UJ5D&contentType=json"
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago%2CUnited%20States/{start_date}/{end_date}?unitGroup=metric&elements=datetime%2Cname%2Ctempmax%2Ctempmin%2Cfeelslike%2Chumidity%2Cprecip%2Cprecipprob%2Cpreciptype%2Csnowdepth%2Cwindgust%2Cwindspeed%2Cwindspeedmax%2Cwindspeedmean%2Cwinddir%2Ccloudcover%2Cvisibility%2Csolarradiation%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription&include=obs%2Cdays&key=2QHAY33FP8938JAMTYLD5UJ5D&options=stnslevel1%2Cnonulls&contentType=json"
test_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago%2CUnited%20States/2022-09-01/2022-09-30?unitGroup=metric&key=2QHAY33FP8938JAMTYLD5UJ5D&contentType=json"
test2 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago%2CUnited%20States/2022-09-01/2022-09-30?unitGroup=metric&elements=datetime%2Cname%2Ctempmax%2Ctempmin%2Cfeelslike%2Chumidity%2Cprecip%2Cprecipprob%2Cpreciptype%2Csnowdepth%2Cwindgust%2Cwindspeed%2Cwindspeedmax%2Cwindspeedmean%2Cwinddir%2Ccloudcover%2Cvisibility%2Csolarradiation%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription&include=obs%2Cdays&key=2QHAY33FP8938JAMTYLD5UJ5D&options=stnslevel1%2Cnonulls&contentType=json"
dates = {}

for i in range(10,13):
    dates[i] = months[i]

for i in range(1, 10):
    dates[i] = months[i]

date_start = "2022-9-01"
date_end = "2022-9-30"



for key,value in dates.items():
    print(key,value)
    if(key > 9):
        year = "2022"
    else:
        year = "2023"

    start_date = f"{year}-{key}-01"
    end_date = f"{year}-{key}-{value}"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago%2CUnited%20States/{start_date}/{end_date}?unitGroup=metric&elements=datetime%2Cname%2Ctempmax%2Ctempmin%2Cfeelslike%2Chumidity%2Cprecip%2Cprecipprob%2Cpreciptype%2Csnowdepth%2Cwindgust%2Cwindspeed%2Cwindspeedmax%2Cwindspeedmean%2Cwinddir%2Ccloudcover%2Cvisibility%2Csolarradiation%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription&include=obs%2Cdays&key=2QHAY33FP8938JAMTYLD5UJ5D&options=stnslevel1%2Cnonulls&contentType=json"
    print(url)
    r = requests.get(url)
    f_out = f"{key}_{year}.json"
    with open(f_out, "w") as file:
        file.writelines(r.text)

#r = requests.get(test2)
#print(r.text)
