import json
from django.core.management.base import BaseCommand
from home.models.user import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for item in data_list:
            # Extract user data from JSON
            first_name = item.get('first_name')
            last_name = item.get('last_name')
            date_of_birth = item.get('date_of_birth')
            gender = item.get('gender')
            phone_number = str(item.get('phone_number'))  # Convert phone_number to string
            email_address = item.get('email_address')
            password = item.get('password')
            user_id = int(item.get('user_id'))  # Convert user_id to integer

            # Create or update user object
            user_obj, created = User.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'date_of_birth': date_of_birth,
                    'gender': gender,
                    'phone_number': phone_number,
                    'email_address': email_address,
                    'password': password
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created User with ID {user_obj.user_id}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated User with ID {user_obj.user_id}'))
