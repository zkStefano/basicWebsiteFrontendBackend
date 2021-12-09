from website import create_app

app = create_app()

if __name__ == '__main__' :
    app.run(debug=True)  #ogni volta che salvo una modifica resetta il server

