from flask import Flask, render_template, flash, request, redirect, url_for
from markupsafe import escape
from photostreamer import image_selection
import os

app = Flask(__name__)
app.secret_key = b'34xc89k6,fi2prghk,.sdn4p5iwp['
@app.route('/')
def index():
    return redirect(url_for('pictures', offset=0))

@app.route('/page/<int:offset>', methods=['GET', 'POST'])
def pictures(offset=0):
    length = 100;
    (pictures, count) = image_selection(offset, offset+length)
    if request.method == 'POST' and request.form.get('action') == 'delete':
        removed = [];
        for selected in request.form.getlist('selection'):
            if (selected in pictures) and (os.path.exists(selected)):
                removed.append(selected)
        if len(removed) >0:
            for path in removed:
                os.remove(path)
            flash('%d pictures removed' % len(removed))
            (pictures, count) = image_selection(offset, offset+length)
    return render_template('pictures.html', pictures=pictures, count=count, offset=offset, length=length)

if __name__ == "__main__":
    app.run(host='127.0.0.1')
