from app import create_app, db
from app.models import User

app = create_app()

def add_sample_data():
    with app.app_context():
        # Clear existing data
        db.session.query(User).delete()
        
        # Add new sample data
        users = [
            User(name='Alice Smith', email='alice@example.com'),
            User(name='Bob Johnson', email='bob@example.com'),
            User(name='Charlie Brown', email='charlie@example.com'),
            User(name='Diana Prince', email='diana@example.com'),
            User(name='Ethan Hunt', email='ethan@example.com')
        ]
        db.session.add_all(users)
        db.session.commit()

if __name__ == '__main__':
    add_sample_data()
    app.run(debug=True)