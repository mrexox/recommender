
class Recommender():
    """
    The class, that accepts the user and csv parsed data
    and calculates the result using logic, required in the task.
    """
    
    def __init__(user: int, data: ndarray):
        self.data = data
        self.user = user
        # Getting the films `user` didn't rate
        self.unwatched = []
        it = nditer(data[user], flags=['f_index'])
        while not it.finished:
            if it[0] == -1:
            self.unwatched.append(it.index)
            it.iternext()

    def getRatingForFilms(self, user, films, data):
        """Returns list of tuples: [(film_index, rating) ... ]"""
        for film in films:
            yield film, getRatingForFilm(film, user)

    def bothHaveRatingCount(self, user1, user2):
        count = 0
        for i in nditer(arange(size(data, 1))):
            if data[user1][i] != -1 and data[user2][i] != -1:
                count += 1
        return count

    def getRatingForFilm(self, film) -> float:
        """Gets the rating of the film. The logic comes here"""
        for user2 in nditer(arange(size(data, 0))):
            m = bothHaveRatingCount(user, user2, data)
            print(user2, m)
        return 1
