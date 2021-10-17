class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


class ErrorsHash:
    db_not_connected = {
        "status_code": 500,
        "message": f"Oops! Something went wrong. There goes a rainbow..."
    }
    default = {
        "status_code": 500,
        "message": f"Internal error"
    }

    def get_error(self, err=""):
        try:
            response = self.__getattribute__(err)
        except:
            response = self.default

        return response
