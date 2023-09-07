import requests # importando api

api_key = "6cf170affad7200cafd1f64ff197eff5" # key api do openweathermap
user_input = input("Insira a cidade: ") # input para selecionar a cidade


weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
# salvando a requisição da api na variavel "weather_data" 

if weather_data.json()['cod'] == '404': # condicional caso a cidade seja inválida (caso a requisição retorne codigo 404)
    print("Nenhuma cidade encontrada.")
else:
    weather = weather_data.json()['weather'][0]['main'] # salvando na variavel weather em json os valores do clima, segundo a requisição
    temp = round(weather_data.json()['main']['temp']) # salvando na variavel temp os valores da temperatura da requisição, e reaproveitando o json
    celsius = ((temp - 32) / 1.8) # conversor de farenheit para celsius

    print(f"O clima em {user_input} é: {weather}") # printando o clima
    print(f"A temperatura em {user_input} é de: {round(celsius, 1)}°C") # printando e convertendo a temperatura