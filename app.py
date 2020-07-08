import json

data = json.load(open('summary.json'))

def Confirmed():
    x = 0
    confirmed_location = data['confirmed']['locations']

    for elems in confirmed_location:
        country = confirmed_location[x]['country']
        latitude = confirmed_location[x]['coordinates']['lat']
        longitude = confirmed_location[x]['coordinates']['long']
        latest_confirmed = confirmed_location[x]['latest']
        print(country + ': ' + 'lat = ' + str(latitude) + ', ' + 'lon= ' + str(longitude) + '\nLatest confirmed : ' + str(latest_confirmed) + "\n")
        x = x + 1

def Deaths():
    x = 0
    deaths_location = data['deaths']['locations']

    for elems in deaths_location:
        country1 = deaths_location[x]['country']
        latitude1 = deaths_location[x]['coordinates']['lat']
        longitude1 = deaths_location[x]['coordinates']['long']
        latest_deaths = deaths_location[x]['latest']
        print(country1 + ': ' + 'lat = ' + str(latitude1) + ', ' + 'lon= ' + str(longitude1) + '\nLatest Deaths : ' + str(latest_deaths) + "\n")
        x = x + 1

def Recovered():
    x = 0
    recovered_location = data['recovered']['locations']

    for elems in recovered_location:
        country = recovered_location[x]['country']
        latitude = recovered_location[x]['coordinates']['lat']
        longitude = recovered_location[x]['coordinates']['long']
        latest_recovered = recovered_location[x]['latest']
        print(country + ': ' + 'lat = ' + str(latitude) + ', ' + 'lon= ' + str(longitude) + '\nLatest Recovery : ' + str(latest_recovered) + "\n")
        x = x + 1

def Total():
    confirmed = data['latest']['confirmed']
    deaths = data['latest']['deaths']
    recovered = data['latest']['recovered']
    print('Confirmed : ' + str(confirmed) + '\nDeaths : ' + str(deaths) + '\nRecovery : ' + str(recovered))


inputData = input('Hello, choose an option, \n1.Show Confirmed cases by country\n2.Show Death cases by country\n3.Show Recovery cases by country\n4.Show Total cases\n:')
if inputData == '1':
    print("\n")
    Confirmed()
    print("\n\nFinished...")
elif inputData == '2':
    print("\n")
    Deaths()
    print("\n\nFinished...")
elif inputData == '3':
    print("\n")
    Recovered()
    print("\n\nFinished...")
elif inputData == '4':
    print("\n")
    Total()
    print("\n\nFinished...")
else:
    print("\n")
    print("Invalid input, please try again later")
