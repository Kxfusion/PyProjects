import webbrowser

class Movie():
    def __init__(self, title, string, image, link):
        self.movie_title = title
        self.movie_image = image
        self.movie_trailer = link
        self.movie_desc = string
        
    def show_trailer(self):
        webbrowser.open_new(self.movie_trailer)
