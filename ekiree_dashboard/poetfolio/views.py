import logging
from urllib.parse import quote_plus, urlencode

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from ed.tools import all_courses
from poetfolio.tools import is_student
from siteconfig.models import HeroImage
from vita.models import Home_page, Menu_item

logger = logging.getLogger(__name__)

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
