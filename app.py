from flask import render_template, redirect, url_for, session
import pandas as pd
import config
import users
import simulations.userdata as usersim
import simulations.get_movie_data as moviedata

app = config.connex_app

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Tables")
def all_tables():
    return render_template("all_tables.html")


@app.route("/TEST")
def test():
    # Examples to get movie data - REMOVE THIS LATER
    #data = moviedata.show_movie_providers('933131')
    data = moviedata.get_movies()
    return data


@app.route("/Tables/Users")
def show_users():
    all_users = users.show_all()
    df = pd.DataFrame(all_users)
    df = df.reindex(columns=["id", "username", "fname", "lname", "role", "email", "registration_date", "last_login", "password"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/users")


@app.route("/Simulation")
def simulation():
    if(session.get("sim_result")):
        result = session.get("sim_result")
        session["sim_result"] = None
    else:
        result = None
    return render_template("simulation.html", result=result)


@app.route("/Simulation/Users")
def simulation_users():
    count = usersim.generate(100)
    if(count > 0): session["sim_result"] = { "error": False, "message": str(count) + " simulated users added!" }
    else: session["sim_result"] = { "error": True, "message": "No simulated users added!" }
    return redirect(url_for('simulation'))


@app.route("/Import")
def import_data():
    return render_template("import_data.html")


if __name__ == "__main__":
    app.add_api(
        config.basedir / "swagger.yml",
        options={
            "swagger_ui": True,
            "swagger_url": "/docs",
        },
    )
    app.run(host="0.0.0.0", port=3000, debug=False)