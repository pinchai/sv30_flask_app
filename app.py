from flask import Flask, render_template
from product import  pro_list

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('index.html')

@app.get('/about')
def about():
    return 'This is the about page.'


@app.get('/products')
def get_products():
    return pro_list


if __name__ == '__main__':
    app.run()
