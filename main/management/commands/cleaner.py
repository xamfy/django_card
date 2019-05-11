from django.core.management import BaseCommand
import os


class Command(BaseCommand):
    def handle(self, **options):
        mydir = 'media/generated'
        filelist = [f for f in os.listdir(mydir) if f.endswith(".jpg")]
        for f in filelist:
            os.remove(os.path.join(mydir, f))
