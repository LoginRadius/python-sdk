import urllib
import simplejson

class LoginRadius:
    def __init__(self, request, api_secrete):
        self.is_authenticated = False
        if "token" in request.POST:
            validate_url = "http://hub.loginradius.com/userprofile.ashx?token=%s&apisecrete=%s" % (request.POST['token'], api_secrete)
            response = urllib.urlopen(validate_url)
            json_response = response.read()
            if json_response:
                self.user_profile=simplejson.loads(json_response)
                if "ID" in self.user_profile and self.user_profile["ID"]:
                    self.is_authenticated = True
					