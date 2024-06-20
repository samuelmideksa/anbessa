from django.urls import path
from routes import views as routes_views

urlpatterns = [
    path('view', routes_views.view, name='view_routes'),
    path('create-route', routes_views.create, name='create_route'),
    path('<int:route_id>/<slug:route_name>/update', routes_views.update,
         name='update_route'),
    path('<int:route_id>/<slug:route_name>/delete', routes_views.delete,
         name='delete_route'),
    path('', routes_views.all_routes, name='all_routes'),
    path('<int:route_id>', routes_views.route_detail, name='route_detail'),
    path('search/', routes_views.search_view, name='search'),
]
