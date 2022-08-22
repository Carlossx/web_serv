
# consumindo uma api com sanic


from sanic import Sanic
from sanic import response
import requests
app=Sanic(name="myAplication")

 #rota para api do dolar
      

@app.route("/",methods=["GET"])
async def main(request):
    r=requests.get('http://economia.awesomeapi.com.br/all/USD-BRL')
    valor=r.json()['USD']['high']

    return response.html(f'<b>O valor do dólar é R${valor}</b>',

    
    )


   # return response.text(f'O valor do dólar é R${valor}')

app.run(host="0.0.0.0",port=3000,workers=4)