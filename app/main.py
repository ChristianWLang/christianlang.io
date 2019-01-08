"""
christianlang.io website.
"""
# Author: Christian Lang <me@christianlang.io>

from flask import Flask, render_template


def main():

    app = Flask(__name__, static_url_path = '/static')

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run('0.0.0.0', port = 8080)

    return
if __name__ == '__main__':
    main()
