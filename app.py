from flask import Flask, redirect, render_template, request, url_for
from movie_web_app.datamanager.json_data_manager import JSONDataManager

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
        data_manager.add_user(name)
        return redirect(url_for('users_list'))
    return render_template('add_user.html')

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    """Handle the form for adding a new movie to a user's favorites."""
    # if request.method == 'POST':
    #     # Process the form data and add the new movie
    # return render_template('add_movie.html')

@app.route('/update_movie', methods=['GET', 'POST'])
def update_movie():
    """Handle the form for updating a movie in a user's favorites."""
    # if request.method == 'POST':
    #     # Process the form data and update the movie
    # return render_template('update_movie.html')

@app.route('/delete_movie', methods=['GET', 'POST'])
def delete_movie():
    """Handle the form for deleting a movie from a user's favorites."""
    # if request.method == 'POST':
    #     # Process the form data and delete the movie
    # return render_template('delete_movie.html')

if __name__ == '__main__':
    app.run(debug=True)
