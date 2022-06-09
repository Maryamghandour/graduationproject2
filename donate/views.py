from importlib.metadata import requires
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

from profiles import models as profiles_models
import stripe

stripe.api_key = "sk_test_51KzIRVH3gADV7GwbEh2Ej1cS2qIp9Q5qPUbagmLWm2F9L9wDf9NfdQEBUMwaXkT4hnaU2T7Lar2MCsFI9wGTPiIr00tow45fZu"

# Create your views here.


def index(request):
    user = request.user
    context = {"title": "Donate"}
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
        context["volunteer"] = volunteer
    return render(request, "index.html", context)


def charge(request):
    if request.method == "POST":

        amount = int(request.POST["amount"])

        customer = stripe.Customer.create(
            email="test@email.com",
            name="test name",
            source=request.POST["stripeToken"],
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency="usd",
            description="Donation",
        )

    return redirect(reverse("success", args=[amount]))


def successMsg(request, args):
    user = request.user
    context = {"title": "Donate success"}
    amount = args
    context["amount"] = amount
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
        context["volunteer"] = volunteer
    return render(request, "success.html", context)
