from DB_APP import create_app

app = create_app()

# APP START
if __name__ == '__main__':
    app.run(debug=True)
