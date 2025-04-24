from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'gologicinstitute123'  # Use a secure key in production

# ---- Database Connection Helper ----
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# ---- Routes ----

@app.route('/')
def homepage():
    user = session.get('user')
    email = session.get('email')
    course = session.get('course')
    return render_template('gologic_homepage.html', user=user, email=email, course=course)

@app.route("/courses")
def courses():
    return render_template("courses.html", user=session.get("user"))

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html", user=session.get("user"))

@app.route("/about")
def about():
    return render_template("about.html", user=session.get("user"))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(f"Message from {name} ({email}): {message}")
        flash("✅ Thank you! Your message has been received.")
        return redirect(url_for("contact"))

    return render_template("contact.html", user=session.get("user"))

# ---- Login ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html", error="Please fill in all fields.")

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).fetchone()
        conn.close()

        if user:
            session["user"] = user["name"]
            session["email"] = user["email"]
            return redirect(url_for("homepage"))
        else:
            return render_template("login.html", error="Invalid email or password.")
    
    return render_template("login.html")

# ---- Register ----
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Email already exists.")
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    user = {
        'name': session.get('user'),
        'email': session.get('email')
    }
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))

# ---- Run the App ----
if __name__ == '__main__':
    app.run(debug=True, port=5253)
