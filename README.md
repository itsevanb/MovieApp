# MovieWeb App

MovieWeb App is a Python-based web application built using the Flask micro web framework. The app allows users to manage their favorite movies. Users can add, update, delete, and view movies. User authentication is also supported with features like registration, login, and logout.

## Key Features

- **User Registration:** New users can register by providing a username and password.
- **User Authentication:** Users can log in and log out of the application. User credentials are verified during login.
- **Profile Management:** Users can view and edit their profile information.
- **Movie Management:** Users can add their favorite movies to their profile. Each movie is fetched from the OMDB API using the movie's title. Users can also update and delete movies from their list.

## Code Structure

The application's codebase is divided into two main parts:

- **Flask Application (`app.py`):** This is the main entry point of our application. It contains all the routes and views for our app.
- **JSON Data Manager (`json_data_manager.py`):** This is our custom data manager that handles all data operations. It reads from and writes to a JSON file, simulating a database.

## Technologies Used

- **Python:** The back-end logic is written in Python.
- **Flask:** Flask is a micro web framework written in Python. It doesn't require particular tools or libraries, allowing you to choose the libraries you want to use.
- **OMDb API:** The Open Movie Database (OMDb) API is a free web service to obtain movie information. We use it to fetch movie details when a user adds a new movie.
- **JSON:** JSON files are used to simulate a database in this application.
- **HTML/CSS:** HTML is used to structure the web content and CSS is used for styling.

## How to Run the Application

1. Clone the repository to your local machine.
2. Install the required Python packages using pip: `pip install -r requirements.txt`.
3. Set the environment variable `SECRET_KEY` to a secret key of your choice.
4. Run the application using the command: `python app.py`.

Please note that the OMDB API requires an API key, which is set to 'a1c766c0' in the `app.py` file. If you want to use your own API key, you will need to replace this value.

## Testing

We recommend both unit tests and manual testing to ensure all functionalities are working as expected. 

*Please note that this is a basic application and does not cover all potential edge cases. For instance, there is no handling of simultaneous updates from different users. This is a learning project and should not be used as is in a production environment.*

## Future Improvements

- Implement a real database instead of using JSON files to store data.
- Add more robust error handling and input validation.
- Implement more features like sorting and filtering movies, adding movies to watchlist, user ratings and reviews, etc.

Contributions are welcome! Please make a pull request.

## License

This project is open source, under the [MIT License](https://choosealicense.com/licenses/mit/).
