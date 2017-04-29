import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about toys that are secretly alive",
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

incep = media.Movie("Inception",
                        "A team of people enter and manipulate dreams",
                        "Inception_(2010)_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

find_nemo = media.Movie("Finding Nemo",
                        "A dad goes on a journey through the ocean to find his son",
                        "Finding_Nemo.jpg",
                        "https://www.youtube.com/watch?v=wZdpNglLbt8")

ferris = media.Movie("Ferris Bueller's Day Off",
                        "A young man takes the day off from school",
                        "Ferris_Bueller's_Day_Off.jpg",
                        "https://www.youtube.com/watch?v=R-P6p86px6U")

iron_man = media.Movie("Iron Man",
                        "A rich genius builds a robot suit and fights villains",
                        "Ironmanposter.jpg",
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
#movies = (toy_story, avatar, incep, find_nemo, ferris, iron_man)
#fresh_tomatoes.open_movies_page(movies)

