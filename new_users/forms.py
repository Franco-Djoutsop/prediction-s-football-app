from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Bettor




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Bettor
        fields = ("email", "number")
        
class CustomUserChangeForm(UserChangeForm):
    class Meta: 
        model = Bettor
        fields = ("email", "number")