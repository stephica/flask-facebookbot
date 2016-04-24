

class InvalidTokenGenerator(Exception):
    pass

class NoUserFound(Exception):
    def __init__():
        super().__init__("User not found")


class TokenStore(object):

    def __init__(token_generator):
        self.store = dict()
        self.token_generator = token_generator
        try:
            getattr(token_generator,"gen_token")
        except AttributeError:
            raise InvalidTokenGenerator("Token generator provided is invalid")


    def gen_token():
        return self.token_generator.gen_token()

    def add_user(token):

    def get_facebook_token(utoken):
