from django.contrib import admin
from django.urls import path
from grievance import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- HTML PAGES (What you see) ---
    path('', views.index, name='index'),                  # Home page
    path('login/', views.login_page, name='login_page'),  # Login Screen
    path('signin/', views.signin_page, name='signin_page'), # Signin Screen
    path('dashboard/student/', views.student_dashboard, name='student_dash'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dash'),

    # --- BEHIND THE SCENES ACTIONS (What the code does) ---
    path('api/signup/', views.signup, name='signup_action'), # Logic for signing up
    path('api/login/', views.login, name='login_action'),    # Logic for logging in
]