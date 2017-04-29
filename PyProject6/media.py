import webbrowser

class Movie():
    """Movie stores specific information about a motion picture
    for future reference"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, string, image, link):
        self.movie_title = title
        self.movie_image = image
        self.movie_trailer = link
        self.movie_desc = string        
        
    def show_trailer(self):
        webbrowser.open_new(self.movie_trailer)
