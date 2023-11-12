class HistoryDatabase:
    films = dict()                  # ключ-id фильма;   значение-название фильма
    history = []                    # все фильмы которые посмотрел пользователь i
    films_persons_assoc = dict()    # ключ-фильм;       значение-все person, которые его посмотрели

    def __init__(self):
        self.read_films("/mnt/F/path_without_Russian/Programming/src/lab4/task_1/films.txt")
        self.read_history("/mnt/F/path_without_Russian/Programming/src/lab4/task_1/history.txt")

    def read_films(self, path: str) -> None:
        self.films.clear()
        with open(path, 'r') as f:
            for line in f:
                key, film_name = line.split(',', 1)
                self.films[int(key)] = film_name[:-1] if film_name[-1] == '\n' else film_name

    def read_history(self, path: str) -> None:
        self.history.clear()
        self.films_persons_assoc.clear()
        with open(path, 'r') as f:
            for line in f:
                self.history.append(frozenset(map(int, line.split(','))))
                for id_film in self.history[-1]:
                    self.films_persons_assoc[id_film] = self.films_persons_assoc.setdefault(id_film, []) + [len(self.history) - 1]

    def get_advice(self, views: frozenset) -> int:
        matches = dict()         # ключ-persona; значение-число совпадений
        for views_film in views:
            for id_person in self.films_persons_assoc[views_film]:
                matches[id_person] = matches.setdefault(id_person, 0) + 1
        len_views = len(views)
        priorities = dict()
        for id_person, number_matches in matches.items():
            k = number_matches / len_views
            for id_film in self.history[id_person]:
                priorities[id_film] = priorities.setdefault(id_film, 0) + k

        result = -1
        for id_film in priorities:
            if(id_film not in views):
                result = id_film
                break
        if(result == -1):
            return "Error! Все фильмы уже просмотрены"
        for id_film, prior in priorities.items():
            if(id_film not in views and prior > priorities[result]):
                result = id_film
        return self.films[result]


if __name__ == '__main__':
    base = HistoryDatabase()
    views = frozenset(map(int, input("Введите список просмотренных фильмов в одну строку").split()))
    print(base.get_advice(views))
