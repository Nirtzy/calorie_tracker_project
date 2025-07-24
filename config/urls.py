from django.contrib import admin
from django.urls import path, include  # Add 'include' here
from django.conf import settings
from django.conf.urls.static import static
from foods import views as food_views  # Import the views from your foods app
from django.contrib.auth import views as auth_views

urlpatterns = [
    # When a user goes to the homepage (''), use the 'home' view.
    path('', food_views.home, name='home'),

    path('register/', food_views.register, name='register'),

    # Use Django's built-in LoginView
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Use OUR custom logout view
    path('logout/', food_views.logout_view, name='logout'),

    path('admin/', admin.site.urls),

    # AJAX food search endpoint
    path('foods/search/', food_views.food_search, name='food_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)