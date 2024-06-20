from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Announcement, Image
from .forms import AnnouncementForm, ImageFormSet


@login_required
def create_announcement(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES)

        if announcement_form.is_valid() and image_formset.is_valid():
            announcement = announcement_form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()

            for form in image_formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(announcement=announcement, image=image)

            return redirect('announcement_detail', announcement_id=announcement.id)
    else:
        announcement_form = AnnouncementForm()
        image_formset = ImageFormSet()

    context = {
        'announcement_form': announcement_form,
        'image_formset': image_formset,
    }
    return render(request, 'announcements/create_announcement.html', context)


@login_required
def announcement_detail(request, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    images = announcement.images.all()
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement, 'images': images})


def all_announcements(request):
    announcements = Announcement.objects.order_by('-created_at')  # Order by created_at descending
    return render(request, 'announcements/all_announcements.html', {'announcements': announcements})