from flask import Flask, render_template, request

app = Flask(__name__)

# ================= HOME =================
@app.route('/')
def home():
    return render_template('index.html')

# ================= MEMBERSHIP =================
@app.route('/membership')
def membership():
    return render_template('membership.html')

# ================= SELECT PLAN =================
@app.route('/select_plan', methods=['POST'])
def select_plan():
    plan = request.form.get('plan')
    return f"✅ You selected the {plan} plan!"

# RUN
if __name__ == '__main__':
    app.run(debug=True)