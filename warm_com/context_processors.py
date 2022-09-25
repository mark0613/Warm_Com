from django.conf import settings


def liff_id(request):
    return { "liff_id" : settings.LIFF_ID }
