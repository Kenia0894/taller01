from flask import Flask ,render_template
import requests
from dotenv import load_dotenv,dotenv_values

config = dotenv_values('.env')

app = Flask (__name__)

def get_weather_data(city):
     API_KEY = config['API_KEY']
     url= f'https://api.openweathermap.org/data/2.5/weather?q={ city }&appid={API_KEY}&lang=es&units=metric'
     r= requests.get(url).json()
     print(r)
     return r

@app.route('/KENNYA')
def KENNYA():
   return get_weather_data('Guayaquil')

  

@app.route('/about')
def about():
   return render_template('curriculum.html')

@app.route('/clima')
def clima():
   return 'clima'

@app.route('/PRUEBA')
def PRUEBA():
   clima =get_weather_data('Quito')
   temperatura =str(clima['main']['temp'])
   descripcion= str(clima['weather'][0]['description'])
   icono = str(clima['weather'][0]['icon'])

   r_json={
        'ciudad': 'Quito',
        'temperatura':temperatura,
        'descripcion' :descripcion,
        'icono':icono
   }
   return render_template('weather.html',clima = r_json)
   
if __name__ == '__main__':
    app.run(debug=True)