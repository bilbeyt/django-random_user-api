from django.core.management import BaseCommand
from django.core.management.base import CommandError
from api.models import StudentDetail


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('code', type=str)

    def handle(self, *args, **options):
        code = options.get("code")
        details = StudentDetail.objects.filter(student_code=code)
        if details.exists():
            details.delete()
        else:
            raise CommandError("Detail Not Found")
        
        

