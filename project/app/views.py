from django.shortcuts import render


def main(request):
    return render(request, 'app/main.html')


def about(request):
    return render(request, 'app/about.html')


def contacts(request):
    return render(request, 'app/contacts.html')