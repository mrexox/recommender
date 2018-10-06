from numpy import nditer, ndarray, arange, size
from math import sqrt


class Recommender():
    """
    The class, that accepts the user and csv parsed data
    and calculates the result using logic, required in the task.
    """
    KNN = 7

    def __init__(self, user: int, data: ndarray):
        self.data = data
        self.user = user

        # Getting the films `user` didn't rate
        self.unwatched = []
        for i in range(size(data, 1)):
            if data[user][i] == -1:
                self.unwatched.append(i)

        # Counting similarity metrics, it - iterator over users

        self.averages = {}
        self.sims = {}
        for it in range(size(data, 0)):
            # Counting average rating
            self.averages[it] = self.countAver(it)

            if it == user:
                continue

            # Conting sim - similarity metrics
            self.sims[it] = self.countSim(it)

        # Users that are very closed to the given one
        # Sorted from most to least closed
        self.closestUsers = sorted(self.sims.keys(),
                                   key=self.sims.__getitem__,
                                   reverse=True,
        )

    def recommend(self):
        """Returns list of tuples: [(film_index, rating), ... ]"""
        for film in self.unwatched:
            yield film, self.recommendForFilm(film)

    def recommendForFilm(self, film):
        count = lower = upper = 0
        for i in self.closestUsers:
            if count == self.KNN:
                break
            if self.data[i][film] == -1:
                continue
            upper += self.sims[i] * (self.data[i][film] - self.averages[i])
            count += 1

            lower += abs(self.sims[i])

        return self.averages[self.user] + ( upper / lower )


    def countSim(self, user2) -> float:
        user1 = self.user
        und1 = und2 = sm = 0
        for i in range(size(self.data, 1)):
            if self.data[user1][i] == -1 or self.data[user2][i] == -1:
                continue
            und1 += self.data[user1][i]**2
            und2 += self.data[user2][i]**2
            sm += self.data[user1][i] * self.data[user2][i]

        und1 = sqrt(und1)
        und2 = sqrt(und2)

        return sm / ( und1 * und2 )

    def countAver(self, user):
        s = c = 0
        for i in nditer(self.data[user]):
            if i == -1:
                continue
            s += i
            c += 1

        return s / c
