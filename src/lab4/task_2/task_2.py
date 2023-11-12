import sys


class Human:
    _age = 0
    _name = ""

    def __init__(self, _age: int, _name: str) -> None:
        self._age = _age
        self._name = _name

    def get_print(self) -> str:
        return self._name + ' (' + str(self._age) + ')'

    def __lt__(self, other) -> bool:
        if self._age == other._age:
            return self._name > other._name
        return self._age < other._age


class Group:
    _min = 0
    _max = 0
    _Peoples = []

    def __init__(self, _min: int, _max: int) -> None:
        self._min = _min
        self._max = _max
        self._Peoples = list()

    def add(self, hum: Human) -> Human:
        self._Peoples.append(hum)
        return hum

    def get_print(self) -> str:
        res = ""
        if len(self._Peoples):
            if self._max >= 124:
                res += str(self._min) + '+: '
            else:
                res += str(self._min) + '-' + str(self._max) + ': '

            res += ', '.join(map(lambda x: x.get_print(), reversed(sorted(self._Peoples)))) + '\n'
        return res


def main(inp: list) -> str:
    age_group = [-1] + list(map(int, sys.argv[1:])) + [124]
    groups = []
    for i in range(len(age_group) - 1):
        groups.append(Group(age_group[i] + 1, age_group[i + 1]))

    for inp_line in inp:
        name, age = inp_line.split(',', 1)
        age = int(age)

        l = 0
        r = len(age_group)
        while r - l > 1:
            m = (r + l) // 2
            if age > age_group[m] + 1:
                l = m
            else:
                r = m
        groups[l].add(Human(age, name))

    return ''.join(map(lambda x: x.get_print(), reversed(groups)))


if __name__ == "__main__":
    hum1 = Human(5, "men1")
    hum2 = Human(5, "men2")
    hum3 = Human(6, "men3")
    group = Group(1, 150)
    group.add(hum1)
    group.add(hum2)
    group.add(hum3)
    print(group.get_print())
    inp = []
    inp_line = input()
    while inp_line != "END":
        inp.append(inp_line)
        inp_line = input()

    print(main(inp))