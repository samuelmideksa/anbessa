from django.urls import path
from announcements import views as announcements_views

urlpatterns = [
    path('', announcements_views.all_announcements, name='all_announcements'),
    path('create', announcements_views.create_announcement, name='create_announcement'),
    path('<int:announcement_id>', announcements_views.announcement_detail, name='announcement_detail'),
]
