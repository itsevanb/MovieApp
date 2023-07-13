from flask import Flask, redirect, render_template, request, url_for
from movie_web_app.datamanager.json_data_manager import JSONDataManager
import requests

app = Flask(__name__)
data_manager = JSONDataManager('movies.json')


@app.route('/')
def home():
    """Render the homepage of the application."""
    return render_template('home.html')


@app.route('/users/')
def users_list():
    """Render a list of all users registered in the movie app."""
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
def user_movies(user_id):
    """Display a list of a specific user's favorite movies."""
    movies = data_manager.get_user_movies(user_id)
    return render_template('user_movies.html', movies=movies)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """Handle the form for adding a new user."""
    if request.method == 'POST':
        name = request.form['name']
        try:
            data_manager.add_user(name)
            return redirect(url_for('users_list'))
        except Exception as e:
            print(f"An error occurred while adding a new user: {str(e)}")
            return render_template('error.html', error_message=str(e))
    return render_template('add_user.html')


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    """Handle the form for adding a new movie to a user's favorites. Pull data from the OMDB API."""
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        title = request.form['title'].strip()
        api_key = 'a1c766c0'
        url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}&plot=full"
        try:
            response = requests.get(url)
            movie_data = response.json()
            print(movie_data)  # for debugging
            movie = {
                'id': len(data_manager.get_user_movies(user_id)) + 1,
                'title': movie_data.get('Title', 'Title not available'),
                'year': int(movie_data.get('Year', 0)),
                'rating': float(movie_data.get('imdbRating', 0.0)),
                'poster': movie_data.get('Poster', 'Poster not available'),
                'plot': movie_data.get('Plot', 'Plot not available')
            }
            data_manager.add_movie(user_id, movie)
            return redirect(url_for('user_movies', user_id=user_id))
        except Exception as e:
            print(f"An error occurred while adding a new movie: {str(e)}")
            return render_template('error.html', error_message=str(e))
    return render_template('add_movie.html')


@app.route('/update_movie', methods=['GET', 'POST'])
def update_movie():
    """Handle the form for updating a movie in a user's favorites."""
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        movie_id = int(request.form['movie_id'])
        title = request.form['title']
        rating = float(request.form['rating'])
        updated_movie = {'id': movie_id, 'name': title, 'rating': rating}
        try:
            data_manager.update_movie(user_id, movie_id, updated_movie)
            return redirect(url_for('user_movies', user_id=user_id))
        except Exception as e:
            print(f"An error occurred while updating a movie: {str(e)}")
            return render_template('error.html', error_message=str(e))
    return render_template('update_movie.html')


@app.route('/delete_movie', methods=['GET', 'POST'])
def delete_movie():
    """Handle the form for deleting a movie from a user's favorites."""
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        movie_id = request.form['movie_id']
        try:
            data_manager.delete_movie(user_id, movie_id)
            return redirect(url_for('user_movies', user_id=user_id))
        except Exception as e:
            print(f"An error occurred while deleting a movie: {str(e)}")
            return render_template('error.html', error_message=str(e))
    return render_template('delete_movie.html')


if __name__ == '__main__':
    app.run(debug=True)
