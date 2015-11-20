#import class media to call instances of movies below
import media
#import fresh_tomatoes to convert python code into opening the webbrowser
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A toy has a story wuttt", "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story.showtrailer()

movies = [toy_story]

fresh_tomatoes.open_movies_page(movies)