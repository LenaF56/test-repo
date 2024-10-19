# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
weight = 4
disketa = 1.44
disketa *= 1024 ** 2
how_much = (disketa)//(pages * lines * symbols * weight)
print("Количество книг, помещающихся на дискету:", round(how_much))
