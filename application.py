from flask import Flask
from app.routes.main import main_bp

# 👇 Explicitly set the templates folder
app = Flask(__name__, template_folder="app/templates")
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)

