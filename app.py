from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota GET simples
@app.route("/hello", methods=["GET"])
def hello():
    return {"message": "Olá, João!"}, 200


# Rota que mostra detalhes da requisição
@app.route("/info", methods=["GET", "POST"])
def info():
    return jsonify({
        "method": request.method,
        "headers": dict(request.headers),
        "args": request.args,
        "json": request.get_json(silent=True),
    }), 200


# Rota POST simples
@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.get_json()
    return {"recebido": data}, 201

@app.route("/cache")
def cache():
    resp = jsonify({"msg": "Página cacheada por 60s"})
    resp.headers["Cache-Control"] = "public, max-age=60"
    return resp

@app.route("/set-cookie")
def set_cookie():
    resp = jsonify({"msg": "Cookie definido"})
    resp.set_cookie("usuario", "joao", max_age=3600)
    return resp

@app.route("/get-cookie")
def get_cookie():
    usuario = request.cookies.get("usuario")
    return {"cookie_usuario": usuario}

# Authorization
@app.route("/segredo")
def segredo():
    token = request.headers.get("Authorization")

    if token != "Bearer 12345":
        return {"erro": "Não autorizado"}, 401

    return {"msg": "Acesso permitido!"}

@app.route("/frame-test")
def frame_test():
    resp = jsonify({"msg": "Teste de X-Frame-Options"})
    resp.headers["X-Frame-Options"] = "DENY"
    return resp


if __name__ == "__main__":
    app.run(debug=True)
