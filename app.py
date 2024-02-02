from flask import render_template, request, jsonify
import config
from models import User
from users import read_all

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)