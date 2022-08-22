from sanic import Sanic
from sanic import response
import requests
import fun_modul_speed
app=Sanic(name="myAplication")

 
      

@app.route("/",methods=["GET"])
async def main(request):
    


    return fun_modul_speed.func_speed()


app.run(host="0.0.0.0",port=9000,workers=4)
