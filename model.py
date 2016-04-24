

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


    def gen_token(self):
        return self.token_generator.gen_token()

    def _add_token(self,service,token,uuid=None):
        if uuid ==None:
            uuid = self.gen_token()
        self.store[uuid][service] = token

        return uuid,token

    def _has_token(self,service):
        pass


    def add_facebook_token(self,token,uuid=None):
        return self._add_token("facebook",token,uuid)

    def get_facebook_token(self,uuid):
