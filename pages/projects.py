class Project:
    "A project class from our repository on Github."
    title = ""
    description = ""
    language = ""
    date_created = ""
    size = 0
    stars = 0
    def __init__(self, title, description, language, date_created, size, stars):
        self.title = title
        self.description = description
        self.language = language
        self.date_created = date_created
        self.size = size
        self.stars = stars