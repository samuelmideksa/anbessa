from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from routes.forms import RouteForm, RouteSearchForm
from routes.models import Route
from users.models import User, Employee


def isScheduler(user):
    schedulers = Employee.objects.filter(role='scheduler')
    return user in schedulers


def view(request):
    routes = Route.objects.all()
    return render(request, 'routes/view.html')


@login_required
def create(request):
    # Check if the current user is scheduler
    current_user = User.objects.get(username=request.user.username)
    if not isScheduler(current_user):
        return HttpResponseForbidden("You do not have permission to access this page.")

    if request.method == 'POST':
        route_form = RouteForm(request.POST, request.FILES)
        if route_form.is_valid():
            route_form.save()

            if 'save' in request.POST:
                return redirect('listings')
            elif 'save-and-add-another' in request.POST:
                return redirect('create_route')

    else:
        route_form = RouteForm()
        return render(request, 'routes/create.html',
                      {'route_form': route_form})


@login_required
def update(request, route_id, route_name):
    # Check if the current user is scheduler
    current_user = User.objects.get(username=request.user.username)
    if not isScheduler(current_user):
        return HttpResponseForbidden("You do not have permission to access this page.")

    route = Route.objects.get(id=route_id)

    if request.method == 'POST':
        route_form = RouteForm(request.POST, request.FILES, instance=route)

        if route_form.is_valid():
            route_form.save()

            return redirect('listings')
    else:
        route_form = RouteForm(instance=route)

    return render(request, 'routes/update.html', {
        'route_form': route_form,
        'route': route,
    })


@login_required
def delete(request, route_id, route_name):
    # Check if the current user is scheduler
    current_user = User.objects.get(username=request.user.username)
    if not isScheduler(current_user):
        return HttpResponseForbidden("You do not have permission to access this page.")

    route = Route.objects.get(id=route_id)
    if request.method == 'POST':
        route.delete()
        return redirect('listings')

    return render(request, 'routes/delete.html', {'route': route})


def all_routes(request):
    form = RouteSearchForm(request.GET or None)
    routes = Route.objects.all()

    if form.is_valid():
        origin = form.cleaned_data.get('origin')
        destination = form.cleaned_data.get('destination')

        if origin:
            routes = routes.filter(origin__icontains=origin)

        if destination:
            routes = routes.filter(destination__icontains=destination)

    return render(request, 'routes/all_routes.html', {'routes': routes, 'form': form})


def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'routes/route_detail.html', {'route': route})


def search_view(request):
    query = request.GET.get('q')
    routes = Route.objects.all()

    if query:
        routes = routes.filter(
            Q(origin__icontains=query) |
            Q(destination__icontains=query)
        )

    context = {
        'routes': routes,
        'query': query,
    }
    return render(request, 'routes/all_routes.html', context)
