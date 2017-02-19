import requests
import base64
import copy
from sjcl import SJCL


class PassmanApi(object):

    ENCRYPTED_VAULT_FIELDS = [u"description", u"username", u"password",
                              u"files", u"custom_fields", u"otp", u"email",
                              u"tags", u"url"]

    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth
        self._auth_headers = {
            "Authorization": "Basic {}".format(
                base64.b64encode(":".join(auth))
            )
        }

    def _send_request(self, verb, endpoint, data=None):
        return getattr(requests, verb)(
            self.base_url + endpoint,
            headers=self._auth_headers,
            data=data
        )

    def get_vaults(self):
        endpoint = "v2/vaults"
        response = self._send_request("get", endpoint).json()
        return response

    def get_vault(self, guid, decrypt=False, key=None):
        endpoint = "v2/vaults/{}".format(guid)
        response = self._send_request("get", endpoint).json()
        if decrypt and key:
            self._decrypt_response(response, key)
        return response

    def _decrypt_response(self, response, key):
        for credential in response["credentials"]:
            for field, value in credential.items():
                if field in self.ENCRYPTED_VAULT_FIELDS:
                    data = eval(base64.b64decode(value))
                    credential[field] = SJCL().decrypt(data, key)

    def new_credential(self, **data):
        endpoint = "v2/credentials"
        response = self._send_request("post", endpoint, data=data).json()
        return response

    def update_credential(self, **data):
        endpoint = "v2/credentials"
        response = self._send_request("patch", endpoint, data=data).json()
        return response
