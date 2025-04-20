from django import forms
from account.models import User

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")  
    name = forms.CharField(label="Name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth"
    )

    class Meta:
        model = User
        fields = ["email", "name", "password", "confirm_password", "gender", "date_of_birth"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")  
