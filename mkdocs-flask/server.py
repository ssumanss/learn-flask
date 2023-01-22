from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.route('/bridge/')
@app.route('/bridge/<path:p1>/')
@app.route('/bridge/<path:p1>/<path:p2>/')
@app.route('/bridge/<path:p1>/<path:p2>/<path:p3>/')
def bridge(p1=None, p2=None, p3=None):
    # Permissions checking...
    # Serve MkDocs's static files requested from CSS files

    if p1 == 'assets' and p2 in ('stylesheets', 'fonts'):
        # CSS fix, e.g. /bridge/css/img/example.png -> /bridge/img/example.png
        return send_from_directory(f'templates/bridge/assets/{p2}/', p3)

    # Serve MkDocs's static files requested from CSS files
    if p1 == 'css' and p2 in ('img', 'fonts'):
        # CSS fix, e.g. /bridge/css/img/example.png -> /bridge/img/example.png
        return send_from_directory(f'templates/bridge/{p2}/', p3)
        
    # Serve MkDocs's static files
    if p1 in ('static', 'assets', 'css', 'js', 'fonts', 'search'):
        return send_from_directory(f'templates/bridge/{p1}/', p2)

    # Serve rendered MkDocs HTML files
    if p3 != None:
        template = f'bridge/{p1}/{p2}/{p3}/index.html'
    elif p2 != None:
        template = f'bridge/{p1}/{p2}/index.html'
    elif p1 != None:
        template = f'bridge/{p1}/index.html'
    else:
        template = 'bridge/index.html'

    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)