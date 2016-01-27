from api import create_app

if __name__ == '__main__':
    app = create_app('flask_config.DevelopmentConfig')
    app.run(debug=True)
