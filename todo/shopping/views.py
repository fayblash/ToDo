from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from accounts.models import Profile
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *

   
def update_shop(request, pk):
    shop = ShoppingItem.objects.get(id=pk)
    form = ShoppingForm(instance=shop)
    if request.method == "POST":
        form = ShoppingForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, 'shopping/update_shop.html', {"shop_edit_form": form})

def delete_shop(request, pk):
    shop = ShoppingItem.objects.get(id=pk)
    shop.delete()
    return redirect("index")