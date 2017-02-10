from flask import Flask, render_template, request
from werkzeug import secure_filename
from collections import Counter

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      data = open(f.filename)
      word_collector = []
      for word in data.read().split():
          word_collector.append(word)
      freq_items = Counter(word_collector)
      freq_items = freq_items.most_common()
      f.save(secure_filename(f.filename))
      return render_template("display.html", freq_items=freq_items)

if __name__ == "__main__":
    app.run(debug = True, port=8080, passthrough_errors=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True