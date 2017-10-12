from media import Movie
from fresh_tomatoes import open_movies_page

# intialize movies instantces
interstellar = Movie("Interstellar",
                     "images/interstellar.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

lion_king = Movie("Lion King",
                  "images/lion_king.jpg",
                  "https://www.youtube.com/watch?v=4sj1MT05lAA")

braveheart = Movie("Braveheart",
                   "images/braveheart.jpg",
                   "https://www.youtube.com/watch?v=wj0I8xVTV18")

shutter_island = Movie("Shutter Island",
                       "images/shutter_island.jpg",
                       "https://www.youtube.com/watch?v=5iaYLCiq5RM")

the_prestige = Movie("The Prestige",
                     "images/the_prestige.jpg",
                     "https://www.youtube.com/watch?v=ijXruSzfGEc")

the_dark_knight = Movie("The Dark Knight",
                        "images/the_dark_knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

gladiator = Movie("Gladiator",
                  "images/gladiator.jpg",
                  "https://www.youtube.com/watch?v=owK1qxDselE")

# intialize list of favourite movies
movies = [interstellar, lion_king, braveheart,
          shutter_island, the_prestige, the_dark_knight, gladiator]

# open webpage of my faourite movies
open_movies_page(movies)
