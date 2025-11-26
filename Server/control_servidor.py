from flask import Flask, request, jsonify
import funciones

tokens_servicios = {
    "XYZ123": "Servicio1"
}

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def post_logs_get():

    token = request.headers.get("Authorization")
    if token not in tokens_servicios:
        return {"error" : "Quien sos, bro?"}, 401

    data = request.get_json()
    if not data:
        return {"error" : "JSON invalido"}, 400
    
    logs = data if isinstance(data, list) else [data]

    resultado = []

    for log in logs:
        valido, msq = funciones.revisar_log(log)

        if valido:
            try:
                log_id = funciones.guardar_log(log)
                resultado.append({"status": "ok", "id_log": log_id})
            except Exception as e:
                resultado.append({"status": "error_db", "error": str(e)})
        else:
            resultado.append({"status": "error_val", "error": msq, "log": log })
    
    return jsonify(resultado), 200

# @app.route('/logs/consultar', methods=['GET'])
# def mostrar_logs():




if __name__ == "__main__":
    app.run(debug=True)