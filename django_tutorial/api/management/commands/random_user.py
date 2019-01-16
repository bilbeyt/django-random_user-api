from django.core.management import BaseCommand
from django.core.management.base import CommandError
from api.models import RandomUser
import requests
import json


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", type=int)

    def handle(self, *args, **options):
        count = options.get("count")
        user_list = []
        for i in range(count, 0, -5000):
            if i > 5000:
                req_count = 5000
            else:
                req_count = i
            res = requests.get("https://randomuser.me/api/?results=" + str(req_count))
            user_infos = json.loads(res.text)["results"]
            user_list = []
            for user_info in user_infos:
                name = user_info["name"]["first"]
                lastname = user_info["name"]["last"]
                mobile_number = user_info["phone"]
                age = user_info["dob"]["age"]
                ru = RandomUser(
                    name=name,
                    last_name=lastname,
                    age=int(age),
                    mobile_number=mobile_number
                )
                user_list.append(ru)
        RandomUser.objects.save_data(user_list)