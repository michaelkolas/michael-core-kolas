from flask import Flask

app = Flask(__name__)

# Register blueprints here
# from app.module import module_blueprint
# app.register_blueprint(module_blueprint)

if __name__ == '__main__':
    app.run(debug=True)