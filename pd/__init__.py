import json

import requests


class PagerDutyAPI(object):

    def __init__(self, api_key, subdomain, user_id):
        self.api_key = api_key
        self.subdomain = subdomain
        self.user_id = user_id

    def _headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': 'Token token=%s' % self.api_key
        }

    def _response(self, r):
        if r.status_code != 200:
            raise Exception("Error talking to PD API, code=%d, text=%s" %
                    (r.status_code, r.text))

        return json.loads(r.text)

    def list_incidents(self, status="triggered"):
        """http://developer.pagerduty.com/documentation/rest/incidents/list
        
        GET https://<subdomain>.pagerduty.com/api/v1/incidents        
        """

        url = "https://%s.pagerduty.com/api/v1/incidents" % self.subdomain
        headers = self._headers()

        d = {
            'assigned_to_user': self.user_id,
            'status': 'triggered',
        }

        data = json.dumps(d)
        r = requests.get(url, headers=headers, data=data)
        resp = self._response(r)

        return resp['incidents']

    def update_incident(self, incident_id, new_status="acknowledged"):
        """http://developer.pagerduty.com/documentation/rest/incidents/update

        PUT https://<subdomain>.pagerduty.com/api/v1/incidents

        (Weird use of PUT)
        """
        url = "https://%s.pagerduty.com/api/v1/incidents" % self.subdomain
        headers = self._headers()
        
        incident = {
            'id': incident_id,
            'status': new_status,
        }
        incidents = [incident]

        d = {
            'incidents': incidents,
            'requester_id': self.user_id,
        }

        data = json.dumps(d)
        r = requests.put(url, headers=headers, data=data)
        return self._response(r)
