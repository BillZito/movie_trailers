#import class media to call instances of movies below
import media
#import fresh_tomatoes to convert python code into opening the webbrowser
import fresh_tomatoes

#create toy_story as new instance of a movie with the necessary info about it and the links to picture and vid
toy_story = media.Movie("Toy Story", "Toys Save Boys", "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#test to see if it prints out/ if storyline saved correctly
#print toy_story.storyline

#create instances of kung pow and school of rock
kung_pow = media.Movie("Kung Pow Enter the Fist", "Spoof of action flick", "https://upload.wikimedia.org/wikipedia/en/5/54/Kungpow.jpg", "https://www.youtube.com/watch?v=GXrAYdSeWY8")

school_of_rock = media.Movie("School of Rock", "A really really good movie about music", "http://www.flickeringmyth.com/wp-content/uploads/2014/08/2003_the_school_of_rock_wallpaper_002.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#create list of movie
movies = [toy_story, kung_pow, school_of_rock]

#pass movies to freshtomatoes.py to open in a web browser
fresh_tomatoes.open_movies_page(movies)