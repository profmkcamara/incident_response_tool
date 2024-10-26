from flask import Flask, render_template, request, redirect, url_for
from models import init_db, add_incident, get_incidents

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create_incident():
    if request.method == "POST":
        incident_type = request.form["incident_type"]
        description = request.form["description"]
        date = request.form["date"]
        status = request.form["status"]
        add_incident(incident_type, description, date, status)
        return redirect(url_for("view_incidents"))
    return render_template("create_incident.html")

@app.route("/incidents", methods=["GET"])
def view_incidents():
    incidents = get_incidents()
    return render_template("view_incidents.html", incidents=incidents)

if __name__ == "__main__":
    app.run(debug=True)
