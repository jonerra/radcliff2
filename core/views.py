from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class PlayerRegistration(CreateView):
    model = Player
    template_name = "register/player_registration.html"
    fields = ["GuardianFirstName", "GuardianLastName", "PlayerFirstName", "PlayerLastName", 'DateOfBirth', 'Street', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Level']
    success_url = reverse_lazy('success')

class VolunteerRegistration(CreateView):
    model = Volunteer
    template_name = "register/volunteer_registration.html"
    fields = ["FirstName", "LastName", "DateOfBirth", "Street", "City", "State", "Zipcode", "PhoneNumber", "Email", "Returning", "Children"]
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"

class PlayerRoster(ListView):
    model = Player
    template_name = "roster.html"

class LeagueUpdate(CreateView):
    model = Update
    template_name = "update/league_update.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('update_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LeagueUpdate, self).form_valid(form)
        
class UpdateList(ListView):
    model = Update
    template_name = "update/update_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(UpdateList, self).get_context_data(**kwargs)
        updates = list(Update.objects.all())
        # update_list = Update.objects.all()[:2]
        update_list = updates[-2:]
        context['update_list'] = update_list
        return context
    
class FieldList(ListView):
    model = Field
    template_name = "fields/field_list.html"
    
class FieldDetail(DetailView):
    model = Field
    template_name = "fields/field_detail.html"

class FieldReservationCreateView(CreateView):
    model = Reservation
    success_url = reverse_lazy('reservation_success')
    template_name = "fields/reservation_form.html"
    fields = ['Date', 'Time', 'FieldID', 'VolunteerID']
    
class FieldReservationSuccess(TemplateView):
    template_name = "fields/reservation_success.html"
    
class FieldReservationUpdateView(UpdateView):
    model = Reservation
    success_url = reverse_lazy('field_list')
    template_name = "fields/reservation_form.html"
    fields = ['Date', 'Time', 'FieldID', 'VolunteerID']
    
class PlayerInfoDetailView(DetailView):
    model = Player
    template_name = "player_info.html"