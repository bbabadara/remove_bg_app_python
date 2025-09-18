from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from rembg import remove
import os

app = Flask(__name__)

# Configuration  dossiers pour stocker  les fichiers uploadés et traités.
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html', message=None, output_file=None)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return render_template('index.html', message="error", output_file=None)

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message="error", output_file=None)

    # Sauvegarder l'image téléchargée
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(input_path)

    try:
        # Lire et traiter l'image pour supprimer le fond
        with open(input_path, 'rb') as f:
            input_data = f.read()

        output_data = remove(input_data)

        # Sauvegarder l'image traitée
        output_file = f'no_bg_{file.filename}'
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_file)
        with open(output_path, 'wb') as out_file:
            out_file.write(output_data)

        # Afficher le message de succès avec le lien de téléchargement
        return render_template('index.html', message="success", output_file=output_file)

    except Exception as e:
        print(e)
        return render_template('index.html', message="error", output_file=None)

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    port=int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
