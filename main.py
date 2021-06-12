from flask import Flask, request, Response, render_template, jsonify
import requests

app = Flask(__name__, static_url_path='/static')


models = {
    "Tony Stark": "TONY STARK",
    "Captain America":  "STEVE ROGERS",
    "Thor": "THOR",
    "Spider Man": "PETER PARKER",
    "Natasha": "NATASHA ROMANOFF",
    "Bruce Banner": "BRUCE BANNER"
}


@app.route("/gpt2", methods=["POST"])
def gpt2():

    context = request.form['context']
    model = request.form['model']

    url =  "https://master-gpt2-mcu-fpem123.endpoint.ainize.ai/mcu"

    length = 80


    data = {
        "name" : model,
        "text" : context,
        "length" : length
    }

    response = requests.post(url, data=data)
    res = response.json()

    return res

@app.route("/")
def main():
    return render_template("index.html")

# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)