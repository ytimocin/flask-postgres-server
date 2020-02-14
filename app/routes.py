from datetime import datetime as dt

from flask import current_app as app, request, make_response

from . import db
from .database.models.account import Account


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }


@app.route('/accounts/', methods=['POST'])
def create_user():
    """Create an account."""
    data = request.get_json()
    name = data['name']
    if name:
        new_account = Account(name=name,
                              created_at=dt.now())
        db.session.add(new_account)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_account} successfully created!")
    else:
        return make_response(f"Name can't be null!")


# @app.route('/products/<barcode>/', methods=['GET'])
# def products(barcode):
#     return openfoodfacts.products.get_product(barcode)
