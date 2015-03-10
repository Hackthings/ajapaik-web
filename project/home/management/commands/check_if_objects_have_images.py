from django.core.management.base import BaseCommand
from project.home.models import Photo


class Command(BaseCommand):
    help = "Check if our database photos have images on disk"

    def handle(self, *args, **options):
        photos = Photo.objects.all()
        for p in photos:
            try:
                p.image
            except:
                print "Exception %d" % p.id