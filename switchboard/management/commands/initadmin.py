from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings

class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()

    def handle(self, *args, **options):
        user_data = {}
        if self.UserModel.objects.count() == 0:
            user_data[self.UserModel.USERNAME_FIELD] = "mojo"
            user_data['password'] = "m0j0@dM1n"
            print('Creating account for %s (%s)' % (username, email))
            admin = self.UserModel.objects.create_superuser(**user_data)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
