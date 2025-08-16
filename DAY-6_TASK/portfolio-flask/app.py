from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-in-production"  # needed for flash messages

# --- Your profile content (easy to edit later) ---
PROFILE = {
    "name": "VADALIYA TIRTH NILESHBHAI",
    "email": "vadaliyatirth@gmail.com",
    "about": (
        "I’m a curious and detail-oriented developer who loves turning ideas into clean, "
        "usable products. I blend logic with design—writing reliable code, organizing data, "
        "and polishing the little UX touches that make software feel great."
    ),
    "skills": [
        "Python", "Java", "HTML", "CSS", "JavaScript",
        "MySQL", "Power BI", "C"
    ],
    # No projects per your request
}

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # very simple validation
        if not name or not email or not message:
            flash("Please fill out all fields.", "error")
            return redirect(url_for("contact"))

        # In a real app you might send an email or save to DB here.
        # For this task we just show a thank-you page.
        return render_template("thanks.html", name=name)

    return render_template("contact.html", profile=PROFILE)

if __name__ == "__main__":
    # Run with: python app.py
    app.run(debug=True)
