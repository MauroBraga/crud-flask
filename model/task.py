class Task:
    def __init__(self, id, title, description, completed=False):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__completed = completed

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "description": self.__description,
            "completed": self.__completed
        }

    @property
    def get_id(self):
        return self.__id

    @property
    def get_title(self):
        return self.__title

    @property
    def get_description(self):
        return self.__description

    @property
    def get_completed(self):
        return self.__completed