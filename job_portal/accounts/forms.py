from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class EmployeeRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [

            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',

        ]


class EmployeeLoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(EmployeeLoginForm, self).clean(*args, **kwargs)
