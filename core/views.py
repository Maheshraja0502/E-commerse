from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from .forms import ContactForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "categories": categories,
        "items": items, 
    })


def contact(request):
    return render(request, 'core/contact.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()
    return render (request, 'core/signup.html', {
        "form":form,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

# def contact_success(request):
#     return render(request, 'contact_success.html')