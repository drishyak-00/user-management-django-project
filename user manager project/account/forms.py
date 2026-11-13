from django import forms
from . models import CustomeUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator ,MaxValueValidator






# def validate_age(value):
#         if value < 18 :
#             raise ValidationError(
#                 "Age must be 18 or above."
#             )  









def validate_first_name(value):
     if len(value) < 3:
          raise ValidationError(
                "Name must contain at least 3 characters."   
          )
                    


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50 ,validators=[validate_first_name])
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(validators=[MinValueValidator(18) , MaxValueValidator(30)])
    email = forms .EmailField()
    password = forms.CharField(max_length=12)



















# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = CustomeUser
#         fields = ['first_name' , 'last_name' , 'age', 'email' , 'password']



    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     if age < 18 :
    #         raise forms.ValidationError(
    #             "Student must be at least 18 years old."
    #         )
    #     return age


    # def clean_first_name(self):
    #     first_name=self.cleaned_data['first_name']
    #     if len(first_name) < 3 :
    #         raise forms.ValidationError(
    #             "Name must contain at least 3 characters."
    #         )
    #     return first_name
