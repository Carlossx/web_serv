

#api sem sanic

import requests
def main():
    r=requests.get('http://economia.awesomeapi.com.br/all/USD-BRL')
    valor=r.json()['USD']['high']
    print(f'Valor do dólar hoje R${valor}')

if __name__=='__main__':
  main()    
