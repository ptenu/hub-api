import random, hashlib

from flask import Response, request, current_app
from flask_restful import Resource

from hub.exts import db
from hub.models.membership import Address, VerifyToken
from hub.models.messaging import Email


class VerifyApi(Resource):

    def get(self, address_text):
        addr = Address.query.filter(Address.line_1==address_text).first()

        if addr is None:
            return {}, 404

        if addr.type != 'EMAIL':
            return {}, 404
        
        if addr.verified:
            return {}, 204
        
        code = random.randint(10000,99999)
        token = VerifyToken(addr.line_1, code)

        db.session.add(token)
        db.session.commit()
        
        self._send_verification_email(addr, code)

        return {
            "code": code
        }, 200


    def post(self, address_text):
        addr = Address.query.filter(Address.line_1==address_text).first()

        if addr is None:
            return {}, 404

        if addr.type != 'EMAIL':
            return {}, 404
        
        if addr.verified:
            return {}, 204
        
        data = request.get_json()

        if data is None:
            return {}, 400

        code = data["code"]

        raw_token = address_text+str(code)
        token = hashlib.sha512(raw_token.encode('UTF-8')).hexdigest()
        
        if VerifyToken.query.get(token) is None:
            return {}, 400
            
        addr.verified = True
        db.session.commit()

        return {}, 204


    def _send_verification_email(self, address, code):
        if address.verified:
            return

        if address.type != 'EMAIL':
            return

        email = Email(
            None,
            'Email verification coded',
            """Your email verification code is:

# {:d}

Enter this on the website to continue.

If you were not expecting this code, please delete this email.""".format(code)
        )

        email.preview_text = 'Verification code is {:d}'.format(code)
        email.type = 'TRN'

        db.session.add(email)

        email.recipients.append(address.person)

        db.session.commit()

        email.send()