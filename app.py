from flask import Flask, render_template, request
from osint_utils.phone import get_phone_info
from osint_utils.email import check_email_breaches
from osint_utils.username import run_socialscan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    query = ""
    if request.method == "POST":
        query = request.form.get("query").strip()
        if query:
            if query.startswith("+") or query.isdigit():
                results['phone'] = get_phone_info(query)
            elif "@" in query:
                results['email'] = check_email_breaches(query)
            results['username'] = run_socialscan(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)