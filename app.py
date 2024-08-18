from flask import Flask, render_template, request
from translate import translate_to_morse, translate_to_text, is_morse_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', output_text = '')

@app.route('/translate', methods = ['POST'])
def translate():
    input_text = request.form['input_text']
    direction = request.form['direction']

    if direction == 'to-morse':
        output_text = translate_to_morse(input_text)

    else:
        output_text = translate_to_text(input_text)

    return render_template('index.html', input_text = input_text, output_text = output_text)

if __name__ == '__main__':
    app.run(debug = True)