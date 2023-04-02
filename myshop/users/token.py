import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from random import randint
import hashlib


class TokenGenerator(PasswordResetTokenGenerator):
    def make_token(self, user, salt=randint(0, 1000)):
        item = hashlib.sha256(str(salt).encode('utf-8')).hexdigest()
        return (
            six.text_type(user.pk)
            + six.text_type(item)
            + six.text_type(user.email_verified)
        )


token_generated = TokenGenerator()
