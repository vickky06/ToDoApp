from django.contrib.auth.forms import UserChangeForm
from .models import Todo

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Todo
        fields = (
            'title',
            'description',
            'status',
            'Time'
        )
