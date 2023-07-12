import json
from .data_manager_interface import DataManagerInterface

class JSONDataManager(DataManagerInterface):
    #Initialize the class with the file name
    def __init__(self, file_name):
        self.file_name = 'movie_web_app/datamanager/' + file_name

    def _read_data(self):
        #Open the file and read the data
        with open(self.file_name, 'r') as file:
            return json.load(file)
        
    def _write_data(self, data):
        #Open the file and write the data
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def get_all_users(self):
        #Return all users
        return self._read_data()
    
    def get_user_movies(self, user_id):
        #Return all movies for a user
        users = self.get_all_users()
        for user in users:
            if user['id'] == user_id:
                return user.get('movies', [])
        return []
    
    def add_user(self, user):
        #Add a new user
        users = self.get_all_users()
        users.append(user)
        self._write_data(users)

    def remove_user(self, user_id):
        #Remove a user
        users = self.get_all_users()
        users = [user for user in users if user['id'] != user_id]
        self._write_data(users)

    def add_movie(self, user_id, movie):
        #Add a movie for a user
        users = self.get_all_users()
        for user in users:
            if user['id'] == user_id:
                user['movies'].append(movie)
        self._write_data(users)

    def update_movie(self, user_id, movie_id, updated_movie):
        #Update a movie for a user
        users = self.get_all_users()
        for user in users:
            if user['id'] == user_id:
                for movie in user['movies']:
                    if movie['id'] == movie_id:
                        movie.update(updated_movie)
        self._write_data(users)

    def removie_movie(self, user_id, movie_id):
        #Remove a movie for a user
        users = users = self.get_all_users()
        for user in users:
            if user['id'] == user_id:
                user['movies'] = [movie for movie in user['movies'] if movie['id'] != movie_id]
        self._write_data(users)