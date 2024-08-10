from flask import Flask, request, render_template, redirect
import random
import string
from database import Urls, Session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['long_url']
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        new_entry = Urls(
            short_url = short_url,
            original_url = original_url
        )

        with Session() as session:
            session.add(new_entry)
            session.commit()
            return f'Shortened URL: {request.url_root}{short_url}'
    else:
        return render_template('home.html')

@app.route("/<short_url>", methods=['GET'])
def jump(short_url):
    with Session() as session:
        entry = session.query(Urls).filter(Urls.short_url == short_url).first()
        if entry:
            return redirect(entry.original_url)
        else:
            return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
