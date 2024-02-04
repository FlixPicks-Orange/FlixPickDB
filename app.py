from flask import render_template, request, jsonify
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml", options={"swagger_ui": True, "swagger_url": "/docs"})


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)