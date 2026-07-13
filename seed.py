"""Seed demo user and films for manual API testing."""

from app import create_app, db
from models import User, Film


def seed():
    app = create_app()
    with app.app_context():
        if User.query.filter_by(username="demo").first():
            user = User.query.filter_by(username="demo").first()
            films = Film.query.limit(3).all()
        else:
            user = User(username="demo", email="demo@example.com")
            films = [
                Film(title="Dune", year=2021, genre="Sci-Fi", director="Denis Villeneuve"),
                Film(title="Paddington 2", year=2017, genre="Comedy", director="Paul King"),
                Film(title="Blade Runner 2049", year=2017, genre="Sci-Fi", director="Denis Villeneuve"),
            ]
            db.session.add(user)
            db.session.add_all(films)
            db.session.commit()

        print("CineLog demo data ready:")
        print(f"  user_id:  {user.id}")
        for film in films:
            print(f"  film_id:  {film.id}  ({film.title})")
        print()
        print("Try these URLs (server must be running: python app.py):")
        print(f"  GET  http://127.0.0.1:5000/films/")
        print(f"  GET  http://127.0.0.1:5000/watchlist/{user.id}")
        print(f"  POST http://127.0.0.1:5000/watchlist/{user.id}/add")


if __name__ == "__main__":
    seed()
