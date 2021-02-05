from django.conf import settings


# The get queryparam which will be provided if we want to count clicks
COUNTCLICK_GET_KEY = getattr(settings, 'COUNTCLICK_GET_KEY', 'countclick')

