from django.shortcuts import render

from announcements.models import Announcement


def home(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, 'core/index.html', {'announcements': announcements})
