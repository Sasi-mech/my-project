from django.shortcuts import render, get_object_or_404
from .models import Club, ClubImage

def home(request):
    featured_clubs = Club.objects.all()[:3]  # Display 3 featured clubs
    clubs = Club.objects.all()  # Fetch all clubs
    gallery_images = ClubImage.objects.all()  # Fetch all gallery images

    return render(request, 'info/home.html', {
        'featured_clubs': featured_clubs,
        'clubs': clubs,
        'gallery_images': gallery_images,
    })

def about(request):
    return render(request, 'info/about.html')

def clubs(request):
    all_clubs = Club.objects.all()  # Get all clubs from the database
    return render(request, 'info/clubs.html', {'all_clubs': all_clubs})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    gallery_images = club.gallery.all()  # Fetch all gallery images for the club
    return render(request, 'info/club_detail.html', {'club': club, 'gallery_images': gallery_images})

def services(request):
    return render(request, 'info/services.html')

def contact(request):
    return render(request, 'info/contact.html')