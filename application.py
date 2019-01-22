import ast
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# globals
labels = []
values = []

@app.route("/")
def index():
    global labels, values
    labels = []
    values = []
    return render_template("index.html", data={"labels":labels, "values":values})


# this refreshes the json data object used by the front end
@app.route("/refresh_data")
def refresh_data():
    global labels, values

    # TODO: probably change kwargs to something more meaningful
    labels.append(len(labels))
    values.append(len(values))

    print("labels now: " + str(labels))
    print("data now: " + str(values))

    return jsonify(sLabel=labels, sData=values)

# this method updates the data object used in the backend
@app.route("/update_data", methods=["POST"])
def update_data():
    global labels, values

    if not request.form or "data" not in request.form:
        return "error", 400

    labels = ast.literal_eval(request.form["label"])
    values = ast.literal_eval(request.form["data"])

    # TODO: print out received labels, values variables

    return "success", 201

if __name__ == "__main__":
    # TODO: pass IP and port
    app.run()