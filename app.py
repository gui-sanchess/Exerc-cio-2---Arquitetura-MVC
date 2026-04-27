from flask import Flask
from App.Controllers.controler import main_bp

# 1. Inicializa o app e diz onde estão os arquivos HTML (Views)
app = Flask(__name__, template_folder='App/Views')

# 2. Registra as rotas que criamos no controlador
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)