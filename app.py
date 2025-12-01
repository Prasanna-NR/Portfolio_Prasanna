from flask import Flask, render_template, send_file, abort
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    try:
        path = os.path.join(app.static_folder, 'Resume_Prasanna_NR.pdf')
        if os.path.exists(path):
            return send_file(path, as_attachment=False)
        else:
            path = os.path.join(app.static_folder, 'Resume_Prasanna_NR (1).pdf')
            if os.path.exists(path):
                return send_file(path, as_attachment=False)
            else:
                abort(404)
    except Exception as e:
        print(f"Error serving resume: {e}")
        abort(404)

@app.route('/view-resume')
def view_resume():
    try:
        path = os.path.join(app.static_folder, 'Resume_Prasanna_NR.pdf')
        if os.path.exists(path):
            return send_file(path, as_attachment=False)
        else:
            path = os.path.join(app.static_folder, 'Resume_Prasanna_NR (1).pdf')
            if os.path.exists(path):
                return send_file(path, as_attachment=False)
            else:
                return "Resume file not found.", 404
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/download-resume')
def download_resume():
    try:
        path = os.path.join(app.static_folder, 'Resume_Prasanna_NR.pdf')
        if os.path.exists(path):
            return send_file(path, as_attachment=True, download_name="Prasanna_NR_Resume.pdf")
        else:
            path = os.path.join(app.static_folder, 'Resume_Prasanna_NR (1).pdf')
            if os.path.exists(path):
                return send_file(path, as_attachment=True, download_name="Prasanna_NR_Resume.pdf")
            else:
                abort(404)
    except Exception as e:
        print(f"Error downloading resume: {e}")
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)