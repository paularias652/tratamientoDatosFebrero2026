from flask import Flask, jsonify, request

app= Flask(__name__) #Inicializar una aplicacion de tipo flask



#url = 'http://localhost:8080/api/'

@app.route('/')
def home(): #Ruta principal
    return jsonify({'mensaje':'Bienvenido a mi microservicio!'})


@app.route('/api/sumar',methods=['POST'])
def sumar():
    data=request.get_json()
    a=data.get('a')
    b=data.get('b')
    
    if a is None or b is None: 
        return jsonify({'error':'Parametros a y b son requeridos'}), 400
    
    return jsonify({'resultado': a + b})

@app.route('/api/info', methods=['GET'])
def info():
    return({
        
        'nombre': 'Microservicio Clase 1 Tratamiento de Datos',
        'version':'1.0.0'
    })


if __name__=='__main__': #Ejecuta mi aplicacion cuando llame al script
    app.run(debug=True, host='0.0.0.0', port = 8080)#cuando ejecutes, corre el app. Host local= 0.0.0.0. Puerto donde va a ser visible la aplicacion