from flask import render_template #rece arquivo html e renderiza
from app import app

print("default")

@app.route("/index")
@app.route("/")
def index():
    print("renderizou########")
    return render_template('index.html')




