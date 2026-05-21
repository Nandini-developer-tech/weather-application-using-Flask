from flask import Flask

app = Flask(__name__)

@app.route('/')
def weather():
    return """
    <html>
    <body>
        <h1>Weather App</h1>
        <h2>City:Ananthapur</h2>
        <h2>Temperature:30C </h3>
        <h2>condition:cloudy </h3>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)