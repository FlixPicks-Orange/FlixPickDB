from flask import render_template, redirect, url_for, session, jsonify
import pandas as pd
import config
import userdata.users as users
import userdata.subscriptions as subscriptions
import userdata.watch_history as watch_history
import userdata.recommendations as recommendations
import content.movies as movies
import content.providers as providers
import content.genres as genres
import simulations.userdata as usersim
import simulations.watchhistory
import simulations.recommendations
import content.discovery.movie_providers as movie_providers
import content.discovery.popular_movies as popular_movies

app = config.connex_app

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Tables")
def all_tables():
    return render_template("all_tables.html")


@app.route("/test")
def test():
    pop_movies = movies.show_popular_movies()
    return jsonify(pop_movies)

@app.route("/find_popular")
def find_popular():
    data = popular_movies.find_popular_movies()
    return jsonify(data)


@app.route("/update_providers")
def update_providers():
    #data = discovery.get_providers_for_movie(1,609681)
    data = movie_providers.find_missing_providers()
    return jsonify(data)


@app.route("/Tables/Users")
def show_users():
    table_data = users.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "username", "fname", "lname", "role", "email", "registration_date", "last_login", "password"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/users")


@app.route("/Tables/Subscriptions")
def show_subscriptions():
    table_data = subscriptions.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "provider_id"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/subscriptions")


@app.route("/Tables/WatchHistory")
def show_watch_history():
    table_data = watch_history.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id", "title", "watched"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Watch History", path="/api/watch_history")


@app.route("/Tables/Recommendations")
def show_recommendations():
    table_data = recommendations.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id", "title", "recommended"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Recommendations", path="/api/recommendations")


@app.route("/Tables/Movies")
def show_movies():
    table_data = movies.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["movie_id", "tmdb_id", "title", "release_date", "runtime", "poster_path", "backdrop_path", "language"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/subscriptions")


@app.route("/Tables/Providers")
def show_providers():
    table_data = providers.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["provider_id", "tmdb_id", "provider_name", "display_priority", "logo_path", "region"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/providers")


@app.route("/Tables/Genres")
def show_genres():
    table_data = genres.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["genre_id", "tmdb_id", "genre_name"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/genres")


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


@app.route("/Simulation/WatchHistory")
def simulation_watch_history():
    simulations.watchhistory.generate()
    session["sim_result"] = { "error": False, "message": "Simulated watch history has been generated!" }
    return redirect(url_for('simulation'))

@app.route("/Simulation/WatchHistoryPattern")
def simulation_patterns_watch_history():
    simulations.watchhistory.generate_pattern()
    session["sim_result"] = { "error": False, "message": "Simulated watch history has been generated!" }
    return redirect(url_for('simulation'))

@app.route("/Simulation/Recommendations")
def simulation_recommendations():
    simulations.recommendations.generate()
    session["sim_result"] = { "error": False, "message": "Simulated Recommendations Populated!" }
    return redirect(url_for('simulation'))
@app.route("/WatchHistory/Clear")
def clear_watch_history():
    


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