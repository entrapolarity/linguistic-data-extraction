from flask import Flask, render_template, request
from extractor import Extractor

app = Flask(__name__)

ext = Extractor()

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template("main.html")


@app.route('/reranker.html', methods=['GET', 'POST'])
def reranker():
    return render_template("reranker.html")

@app.route('/bm25.html', methods=['GET', 'POST'])
def bm25():
    return render_template("bm25.html")

@app.route('/extracted.html', methods=['GET', 'POST'])
def extracted():
    return render_template("extracted.html")


@app.route('/reranker', methods=['POST'])
def answer_reranker():
    
    feature = request.form["feature"]
    language = request.form["language"]
    res, indices, image_files, fname_indices = ext.extract(language, feature, method="Reranker")
    return render_template('extracted.html', res=res, indices=indices, image_files=image_files, fname_indices = fname_indices)

@app.route('/bm25', methods=['POST'])
def answer_bm25():
    
    feature = request.form["feature"]
    language = request.form["language"]
    res, indices, image_files, fname_indices = ext.extract(language, feature, method="BM25")
    return render_template('extracted.html', res=res, indices=indices, image_files=image_files, fname_indices=fname_indices)

if __name__ == '__main__':
    app.run()