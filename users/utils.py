import random
from asgiref.sync import sync_to_async
from .models import UserProfile, Token


import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def generate_code():
    return [random.randint(3,9) for i in range(5)]
    
@sync_to_async
def get_user(chat_id):
    user = UserProfile.objects.get(tg_id=chat_id)
    
    return user


from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from asgiref.sync import sync_to_async

async def get_token(user):
    try:
        # Get all UserProfile objects for this user
        get_objects_sync = sync_to_async(Token.objects.filter, thread_sensitive=True)
        objects = await get_objects_sync(user=user)

        # If there are no objects, return None
        if not objects:
            return None

        # Get the latest object
        latest_object = objects.last()

        # Update all other objects to be inactive
        other_objects = objects.exclude(pk=latest_object.pk)
        update_objects_sync = sync_to_async(other_objects.update, thread_sensitive=True)
        await update_objects_sync(active=False)

        # Return the latest object
        return latest_object

    except ObjectDoesNotExist:
        return None

async def create_token(user, code):
    token = await Token.objects.acreate(
                user=user,
                code = code,
                active=True
            )
    
    return token