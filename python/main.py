from flask import Flask, request
app = Flask(__name__, static_url_path='')

website = "<html><head><title></title><meta charset='utf-8'><link href='../css/design.css' rel='stylesheet' type='text/css'><meta name='viewport' content='width=device-width, user-scalable=no'></head><body><div class='centerText' id='yellowSnapDiv'><img src='../media/logo.png' id='logoIn'></div><div class='centerText' id='redSnapDiv'><button>Iniciar Sesión</button></div><div class='centerText' id='blueSnapDiv'><button>Registrarme</button></div></body></html>"

@app.route('/')
def root():
    return website
