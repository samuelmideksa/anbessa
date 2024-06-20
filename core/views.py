from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from announcements.models import Announcement


def home(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, 'core/index.html', {'announcements': announcements})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'admin/management_dashboard.html')
