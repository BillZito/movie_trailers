# import webbrowser to allow the opneing of web browsers,
import webbrowser

"""
create a class movie that will have the movie contents to be initialized for
different movies in enternainment.py. for each item, the self-categories are
set to the corresponding descriptors passed through in the function description
"""


class Session():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# function to show the trailer using webbrowser by opening the youtube link
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
