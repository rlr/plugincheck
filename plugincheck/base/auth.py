from django.contrib.auth.models import Group

from django_browserid.auth import BrowserIDBackend


class OnlyMozillaBackend(BrowserIDBackend):
    """Backend that only allows *@mozilla.com emails to join.

    They get is_staff bit by default.
    """
    def create_user(self, email):
        if email.endswith('@mozilla.com'):
            # Set the username to the part of the email address before the @
            username = email.split('@')[0]

            # Create the user
            user = self.User.objects.create_user(username, email)

            # Set the staff bit
            user.is_staff = True
            user.save()

            # Add to administrators group
            user.groups.add(Group.objects.get(name='administrators'))

            return user

        return None
