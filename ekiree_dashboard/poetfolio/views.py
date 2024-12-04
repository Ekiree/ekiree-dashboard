import json
import logging
from urllib.parse import quote_plus, urlencode

from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from ed.tools import all_courses
from poetfolio.tools import is_student
from siteconfig.models import HeroImage
from vita.models import Home_page, Menu_item

logger = logging.getLogger(__name__)

# Configuration for Auth0
oauth = OAuth()
oauth.register(
    "auth0",
    client_id = settings.AUTH0_CLIENT_ID,
    client_secret = settings.AUTH0_Client_secret,
    client_kwargs = {
        "scope": "openid profile email",
    },
    server_metadata_url = f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def Index(request):
    menu = Menu_item.objects.order_by("order")
    home = Home_page.objects.order_by("-publish_date")[0]

    user = request.user
    if is_student(request.user):
        studentcourses = all_courses(user)
    else:
        studentcourses = None

    try:
        hero = HeroImage.objects.get(app="default")
    except:
        hero = None
    return render(
        request,
        "base.html",
        {
            "pagename": "Welcome",
            "hero": hero,
            "menu": menu,
            "home": home,
            "usercourses": studentcourses,
        },
    )
