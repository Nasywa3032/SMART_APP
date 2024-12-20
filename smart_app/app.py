from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mengambil data dari form
        normalized_data = np.array([
            [float(request.form['A1_C1']), float(request.form['A1_C2']), float(request.form['A1_C3']), float(request.form['A1_C4']), float(request.form['A1_C5'])],
            [float(request.form['A2_C1']), float(request.form['A2_C2']), float(request.form['A2_C3']), float(request.form['A2_C4']), float(request.form['A2_C5'])],
            [float(request.form['A3_C1']), float(request.form['A3_C2']), float(request.form['A3_C3']), float(request.form['A3_C4']), float(request.form['A3_C5'])],
            [float(request.form['A4_C1']), float(request.form['A4_C2']), float(request.form['A4_C3']), float(request.form['A4_C4']), float(request.form['A4_C5'])]
        ])
        
        weights = np.array([
            float(request.form['weight_C1']),
            float(request.form['weight_C2']),
            float(request.form['weight_C3']),
            float(request.form['weight_C4']),
            float(request.form['weight_C5'])
        ])

        # Hitung skor akhir
        scores = normalized_data @ weights

        # Tentukan alternatif terbaik
        best_alternative_index = np.argmax(scores)
        best_score = scores[best_alternative_index]

        return render_template('result.html', scores=scores, best_alternative=best_alternative_index + 1, best_score=best_score)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)