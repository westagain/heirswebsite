import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('papers.json', 'r') as file:
        papers = json.load(file)
    return render_template('index.html', papers=papers)

@app.route('/paper/<int:paper_id>')
def paper_detail(paper_id):
    with open('papers.json', 'r') as file:
        papers = json.load(file)
    paper = next((p for p in papers if p['id'] == paper_id), None)
    if paper:
        return render_template('paper_detail.html', paper=paper)
    else:
        return "Paper not found", 404

if __name__ == '__main__':
    app.run(debug=True)
