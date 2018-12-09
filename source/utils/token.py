from datetime import datetime, timedelta

import jwt


def encode_jwt(token_data, token_salt):
    # Have to put the "exp" and "iat" headers here instead of the normal headers section because PyJWT has a bug
    return {'token': jwt.encode(
        {
            **token_data,
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'iat': datetime.utcnow()},
        token_salt
    ).decode('ascii')}
