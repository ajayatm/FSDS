class OopsException(Exception):
    pass


if False:
    raise OopsException('Caught an oops')


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))
print(movies)
