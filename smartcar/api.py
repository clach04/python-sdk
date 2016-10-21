from . import const, requester

class Api(object):
    def __init__(self, access_token, vehicle_id=None):
        self.access_token = access_token
        self.vehicle_id = vehicle_id
        self.auth = {
            "Authorization": "Bearer {}".format(access_token)
        }

    def _format(self, endpoint):
        return "{}/{}/{}".format(const.API_URL, self.vehicle_id, endpoint)

    def action(self, endpoint, action, **kwargs):
        url = self._format(endpoint)
        json = { "action": action }
        for k,v in kwargs.items():
            if v:
                json[k] = v

        return requester.call('POST', url, json=json, headers=self.auth)

    def get(self, endpoint):
        url = self._format(endpoint)
        return requester.call("GET", url, headers=self.auth)

    def permissions(self, **params):
        url = self._format("permissions")
        return requester.call("GET", url, headers=self.auth, params=params)

    def disconnect(self):
        url = self._format("application")
        return requester.call("DELETE", url, headers=self.auth)

    def vehicles(self, **params):
        url = const.API_URL
        return requester.call("GET", url, headers=self.auth, params=params)