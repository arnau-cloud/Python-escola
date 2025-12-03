def retorna_ciutats(*ciutats):
        for element in ciutats:
                for subelement in element:
                        yield subelement

ciutats_retornades = retorna_ciutats("ABrcelona", "Tarragona", "Lleida", "Girona")
print(f"\033[33m{next(ciutats_retornades)}\033[0m")
print(f"\033[35m{next(ciutats_retornades)}\033[0m")

def retorna_ciutats(*ciutats):
            for element in ciutats:
                    yield from element

ciutats_retornades = retorna_ciutats("BArcelona", "Tarragona", "Lleida", "Girona")
print(f"\033[35m{next(ciutats_retornades)}\033[0m")
print(f"\033[33m{next(ciutats_retornades)}\033[0m")