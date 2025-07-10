from flask import Blueprint, render_template, request
from app.recommender.recommend import recommend_movies

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template("index.html")

@main_bp.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get('mood')
    results = recommend_movies(mood)
    return render_template("results.html", movies=results)

