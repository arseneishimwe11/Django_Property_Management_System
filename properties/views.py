from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm


@login_required(login_url='/users/login')
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})


@login_required(login_url='/users/login')
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})


@login_required(login_url='/users/login')
def property_update(request, pk):
    property_to_update = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_to_update)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property_to_update)
    return render(request, 'properties/property_update.html', {'form': form})


@login_required(login_url='/users/login')
def property_delete(request, pk):
    property_to_delete = Property.objects.get(pk=pk)
    if request.method == 'POST':
        property_to_delete.delete()
        return redirect('property_list')
    return render(request, 'properties/property_confirm_delete.html', {'property': property_to_delete})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('property_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

