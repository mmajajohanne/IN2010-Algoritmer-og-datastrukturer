import sys


class finn_kattungen:
    def __init__(self) -> None:
        pass

    def les_inn(self):

        input = sys.stdin.read
        data = input().splitlines()

        katt_pos = int(data[0])  # første linje er posisjonen til katten
        foreldre = {}  # ordbok for barn med tilhørende forelder

        for linje in data[1:]:
            if linje == "-1":
                break
            else:
                noder = list(map(int, linje.split()))
                f = noder[0]
                # legger inn barn som nøkkel og forelder som verdi
                for barn in noder[1:]:
                    foreldre[barn] = f

        return katt_pos, foreldre

    def finn_sti(self, pos, foreldre):
        sti = []
        self._rekursiv_leting(pos, foreldre, sti)
        return sti

    def _rekursiv_leting(self, pos, foreldre, sti):
        # legg til gjeldende posisjon i stien
        sti.append(pos)
        # hvis posisjon har en forelder, fortsett oppover treet
        if pos in foreldre:
            self._rekursiv_leting(foreldre[pos], foreldre, sti)


def main():
    katt = finn_kattungen()
    l = katt.les_inn()
    print(katt.finn_sti(l[0], l[1]))


if __name__ == "__main__":
    main()
