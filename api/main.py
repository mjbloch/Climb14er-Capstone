from app import app


if __name__ == '__main__':
    app.run(debug=True, port=8080, static_folder='../build', static_url_path='/')