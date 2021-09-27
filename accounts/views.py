from django.shortcuts import render

# Create your views here.

def accounts(request):
    context = { }
    return render(request, "accounts/accounts.html", context)