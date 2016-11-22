import media
import fresh_tomatoes
toystory = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://goo.gl/dMlfOA", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

bahubali = media.Movie("Bahubali", "A daring man becomes involved in a decades old feud",
                       "https://goo.gl/U9MeHw",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

movies = [toystory, avatar, bahubali]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
