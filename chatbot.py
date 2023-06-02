from flask import Flask, request, jsonify
from flask_cors import CORS

class Chatbot:
    def process_input(self, message):
        options = [
             "Gestiones sobre pagos",
             "Instalaciones/Problemas técnicos",
             "Informacion sobre consumos",
             "Informacion sobre deuda vigente",
             "Comunicarme con un asesor"
            ]
        if message.lower() == "opciones" or message.lower() == "hola":
            welcome_message = "Bienvenido, elija una opción para ayudarlo"
            response = [welcome_message] + options
        else:
            follow_message = "Para seguir, deberá elegir una opción"
            response = [follow_message] + options
        return response

    def process_option(self, option):
        switcher = {
            "1": "Para solucionar problemas con el pago, deberá comunicarse más tarde",
            "2": "Para instalaciones o problemas técnicos, debe comunicarse con atención al cliente al 0800-33-333",
            "3": "DNI",
            "4": "Deuda",
            "5": "Conectando con un asesor..."
        }
        response = switcher.get(option)
        return response

# Crear una instancia del Chatbot
chatbot = Chatbot()

# Crear una aplicación Flask
app = Flask(__name__)
CORS(app)

# Ruta para recibir y responder a las solicitudes POST
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    
    if message.lower() in ["1", "2", "3", "4", "5"]:
        option = message.lower()
        response = chatbot.process_option(option)  # Procesar la opción seleccionada
    else:
        response = chatbot.process_input(message)  # Procesar el mensaje
        
    return jsonify({'response': response})

# Ejecutar la aplicación Flask en el servidor local en el puerto 5050
if __name__ == '__main__':
    app.run(port=5050)
