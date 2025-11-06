from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

months = {
    "january": "Listen to music for at least 2 hours",
    "february": "Procastinate for at least 6 hours",
    "march": "Watch reels for at least 3 hours",
    "april": "Watch reels for at least 3 hours",
    "june": "Watch reels for at least 3 hours",
    "july": "Watch reels for at least 3 hours",
    "august": "Watch reels for at least 3 hours",
    "september": "Watch reels for at least 3 hours",
    "october": "Watch reels for at least 3 hours",
    "november": "Watch reels for at least 3 hours",
    "december": "Watch reels for at least 3 hours",
}

def challenges(request):
    challenge_links = "<a><a>"


def monthly_challenge(request, month):
    try:
        templateString = render_to_string("challenges/challenge.html")
        return HttpResponse(templateString)
    except:
        return HttpResponse("Month not supported")


def monthly_challenge_by_number(request, month):
    try:
        if month < 1 or month > 11:
            return HttpResponse("Month not supported")
        monthNumbers = list(months.keys())
        monthSelected = monthNumbers[month - 1]
        url_redirect = reverse("month_challenge", args=[monthSelected])
        return HttpResponseRedirect(url_redirect)
    except:
        return HttpResponse("This month is not suported")
