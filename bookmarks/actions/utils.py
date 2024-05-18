from django.contrib.contenttypes.models import ContentType
from .models import Action

def create_action(user, action, target=None):
    action = Action(user=user, action=action, target=target)
    action.save()