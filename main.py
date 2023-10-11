from website import create_app # can import anythign from __init_.py

app = create_app()
if __name__ == '__main__':
    app.run(debug = True) # automatically will update the website after every change
    