# app.py
from flask import Flask
from models.db import db
from import_csv import import_csv_to_db
import os


def create_app():
    app = Flask(__name__)

    # Configure your database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:LeaPsql@localhost/StockCompaniesData'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db with the app
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()


@app.route('/')
def initialize_app():
    return 'App initialized! Visit /import-csv to import data.'


@app.route('/import-csv')
def import_csv():
    try:
        csv_folder = os.path.join(os.path.dirname(__file__), 'csv last')
        import_csv_to_db(csv_folder)
        return 'CSV import completed successfully!'
    except Exception as e:
        return f'Error during import: {str(e)}', 500


if __name__ == '__main__':
    app.run(debug=True)
