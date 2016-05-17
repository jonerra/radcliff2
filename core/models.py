from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from phonenumber_field.modelfields import PhoneNumberField

returning_choices = (
(0, ''),
(1, 'Yes'),
(2, 'No'),
)

level_choices = (
(0, ''),
(1, 'PeeWee (Ages 8-10)'),
(2, 'Minors (Ages 10-12)'),
(3, 'Majors (Ages 12-14)'),
)

time_choices = (
(0, ''),
(1, '8:00 AM - 10:00 AM'),
(2, '10:00 AM - 12:00 PM'),
(3, '12:00 PM - 2:00 PM'),
(4, '2:00 PM - 4:00 PM'),
(5, '4:00 PM - 6:00 PM'),
)

# Create your models here.
class Player(models.Model):
    GuardianFirstName = models.CharField('Guardian First Name', null=True, blank=True, max_length=300)
    GuardianLastName = models.CharField('Guardian Last Name', null=True, blank=True, max_length=300)
    PlayerFirstName = models.CharField('Player First Name', max_length=300)
    PlayerLastName = models.CharField('Player Last Name', max_length=300)
    DateOfBirth = models.DateField('Date Of Birth')
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField('Zip Code')
    PhoneNumber = models.CharField(max_length=50, verbose_name='Phone Number', help_text="Please use the following format: <em>555-555-5555</em>.")
    Level = models.IntegerField(choices=level_choices, default=0)

    def __unicode__(self):
        return self.GuardianLastName
        
    def get_absolute_url(self):
        return reverse('player_detail', args=[self.id])

class Volunteer(models.Model):
    FirstName = models.CharField('First Name', max_length=300)
    LastName = models.CharField('Last Name', max_length=300)
    DateOfBirth = models.DateField('Date Of Birth')
    Street = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    State = models.CharField(max_length=300)
    Zipcode = models.IntegerField('Zip Code')
    PhoneNumber = models.CharField(max_length=50, verbose_name='Phone Number', help_text="Please use the following format: <em>555-555-5555</em>.")
    Email = models.EmailField(max_length=300)
    Returning = models.IntegerField(choices=returning_choices, default=0)
    Children = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.LastName

class Field(models.Model):
    FieldName = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Picture = models.ImageField(upload_to='images', default='images', null=True)
    
    def __unicode__(self):
        return self.FieldName
        
    def get_absolute_url(self):
        return reverse('field_detail', args=[self.id])

class Position(models.Model):
    PositionDescrip = models.CharField(max_length=300)

class VolunteerAssignment(models.Model):
    VolunteerID = models.ForeignKey(Volunteer)
    PositionID = models.ForeignKey(Position)
    Year = models.IntegerField()

class Division(models.Model):
    Level = models.CharField(max_length=300)

class Team(models.Model):
    TeamName = models.CharField(max_length=50)
    VolunteerID = models.ForeignKey(Volunteer)
    DivisionID = models.ForeignKey(Division)
    Year = models.IntegerField()

class Roster(models.Model):
    TeamID = models.ForeignKey(Team)
    PlayerID = models.ForeignKey(Player)

class Reservation(models.Model):
    FieldID = models.ForeignKey(Field, verbose_name='Field')
    VolunteerID = models.ForeignKey(Volunteer, verbose_name='Coach')
    Date = models.DateField()
    Time = models.IntegerField(choices=time_choices, default=0)
    
    def __unicode__(self):
        return u'%s %s' % (self.Date, self.VolunteerID)
    
    class Meta:
        unique_together = ('Date', 'Time', 'FieldID')
    
class Update(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
