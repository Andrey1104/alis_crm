from django.urls import path
from . import views
from .views import CalendarView, EventCreateView, EventDetailView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/month/', views.monthly_calendar_view, name='monthly_calendar'),
    path('create_event/', EventCreateView.as_view(), name='create_event'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

]

app_name = 'task'
