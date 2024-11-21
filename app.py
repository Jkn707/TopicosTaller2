from flask import Flask, jsonify, render_template
import random, socket

app = Flask(__name__)

ARRAY = [
    {"id": 1, "nombre": "El Pote", "altura": "1.70m", "habilidad": "Destapar guaro de un soplido", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002402.png", "frase": "Parce, me la prestás un ratico, te la devuelvo enterita, te lo juro."},
    {"id": 2, "nombre": "El Cucho", "altura": "1.67m", "habilidad": "Pedir fiado sin pena", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002602.png", "frase": "Eso antes no pasaba, todo empezó a dañarse con los pelados de ahora."},
    {"id": 3, "nombre": "El Ñato", "altura": "1.82m", "habilidad": "Hacer que los chinos respeten", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002648.png", "frase": "¡Uy no, qué culebra la que tengo, pero ahí la vamos llevando!"},
    {"id": 4, "nombre": "El Chopo", "altura": "1.78m", "habilidad": "Desarmar una moto en menos de 5 minutos", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002717.png", "frase": "Hermano, la calle es dura, pero aquí seguimos firmes como riel del metro."},
    {"id": 5, "nombre": "El Tato", "altura": "1.74m", "habilidad": "Colarse en la fila del metro", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002741.png", "frase": "Vea, socio, usted me da confianza, hagámosle pues al negocio."},
    {"id": 6, "nombre": "El Mono", "altura": "1.90m", "habilidad": "Identificar perico de mala calidad", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002837.png", "frase": "¿Cómo así que no entra? ¿No sabe quién soy yo o qué?"},
    {"id": 7, "nombre": "El Pecas", "altura": "1.54m", "habilidad": "Negociar cualquier cosa en la plaza", "imagen": "https://storage.googleapis.com/pokeneas-jamg/neas/Screenshot%202024-11-21%20002859.png", "frase": "Tranquilo, papi, yo me encargo, aquí no hay lío."},
]


@app.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(ARRAY)
    contenedor_id = socket.gethostname()
    return render_template('index.html', pokenea=pokenea, contenedor_id=contenedor_id)

@app.route('/json', methods=['GET'])
def api_random():
    pokenea = random.choice(ARRAY)
    contenedor_id = socket.gethostname()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
