import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about toys that are secretly alive",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

incep = media.Movie("Inception",
                        "A team of people enter and manipulate dreams",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

find_nemo = media.Movie("Finding Nemo",
                        "A dad goes on a journey through the ocean to find his son",
                        "https://www.youtube.com/watch?v=wZdpNglLbt8")

ferris = media.Movie("Ferris Bueller's Day Off",
                        "A young man takes the day off from school",
                        "https://www.youtube.com/watch?v=R-P6p86px6U")

iron_man = media.Movie("Iron Man",
                        "A rich genius builds a robot suit and fights villains",
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = (toy_story, avatar, incep, find_nemo, ferris, iron_man)
fresh_tomatoes.open_movies_page(movies)

