from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return 'Welcome to the Flask Web Application!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Thank you, {name}! We received your email as {email}."
    return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
