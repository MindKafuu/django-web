from django.views.generic import TemplateView
import requests

from .models import Product

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class Start(TemplateView):
    template_name = "home.html"
    model = Product

    def generate_token(self, url):
        body = {
            "username":"",
            "password":""
        }
        response = requests.post(url, json=body)
        return response.json()

    def get_context_data(self, *args, **kwargs):
        token = self.generate_token("http://127.0.0.1:8000/bigAPI/authen/token-login")
        auth_token = BearerAuth(token['access_token'])

        url = 'http://127.0.0.1:8000/bigAPI/test/command'
        body = {
            "header": {
                "sysid":"CST",
                "requestID":""
            },
            "name": "Pandoraedo",
            "subscription": "12 Years Family",
            "credit": 67.23,
            "country": "Thailand"
        }

        response = requests.post(url, json=body, auth=auth_token)
        context = super(Start, self).get_context_data(*args, **kwargs)
        games = self.model.objects.all()
        context['games'] = games
        context['response'] = response.json()

        return context

class SubscriptionListView(TemplateView):
    template_name = "sub_list.html"

    def generate_token(self, url):
        body = {
            "username":"",
            "password":""
        }
        response = requests.post(url, json=body)
        return response.json()

    def get_context_data(self, *args, **kwargs):
        token = self.generate_token("http://127.0.0.1:8000/bigAPI/authen/token-login")
        auth_token = BearerAuth(token['access_token'])

        url = 'http://127.0.0.1:8000/bigAPI/test/users'
        body = {
            "header": {
                "sysid":"CST",
                "requestID":""
            },
            "subscription": "3 months"
        }

        response = requests.post(url, json=body, auth=auth_token)
  
        context = super(SubscriptionListView, self).get_context_data(*args, **kwargs)
        context['users'] = response.json()

        return context
