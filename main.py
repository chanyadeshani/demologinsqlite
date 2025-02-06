from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Some hard to guess key'


@app.route('/')
def index():
    return render_template("home.html")  # Add you dashboad here


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Can get name of the user from database here
        user_name = request.form['user_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            db.add_user_data(user_name, password)

        return redirect(url_for('login'))
    else:
        return render_template("register.html")


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # Can get name of the user from database here
        username = request.form['user_id']
        password = request.form['password']
        print(username, password)
        stored_password = db.get_userdata(username)[0][2]
        print(stored_password)
        if password == stored_password:
            session['user_id'] = request.form['user_id'],

            return redirect(url_for('index'))
        else:
            return render_template("login.html", message="error")
    return render_template("login.html")


if __name__ == '__main__':
    db = database.Database()
    db.create_user_tbl()

    app.run(debug=True)
