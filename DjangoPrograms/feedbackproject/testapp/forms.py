from django import forms
from django.core import validators

#*custom validators 
# def starts_with_s(value):
#   print('starts_with_s function execution')
#   if value[0].lower() !=0:
#            raise forms.ValidationError('Name should be starts with s or S')

# def gmail_validation(value):
#     print('Checking for gmail validation')
#     if value[-10:] != '@gmail.com':
#         raise forms.ValidationError('Mail extension should be gmail')
    
# class Feedbackform(forms.Form):
#                 name= forms.CharField(validators=[starts_with_s])
#                 rollno = forms.IntegerField()
#                 email = forms.EmailField(validators=[gmail_validation])
#                 feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])


                # def clean_name(self):
                #         print("Validating name field")
                #         input_name = self.cleaned_data['name']
                #         if len(input_name)<4:
                #                 raise forms.ValidationError("The minimun lenght should be 4 letters...") #!automatically this message shows in form html 
                #         return input_name
                
                # def clean_rollno(self):
                #         print('Validating RollNo Field')
                #         input_rollno = self.cleaned_data['rollno']
                #         return input_rollno
                
                # def clean_email(self):
                #         print('Validating Email Field')
                #         input_email = self.cleaned_data['email']
                #         return input_email
                
                # def clean_feedback(self):
                #         input_feedback = self.cleaned_data["feedback"]
                #         if len(input_feedback)<10 :
                #                 raise forms.ValidationError("The minimun lenght should be 10 letters...")
                #         return input_feedback
    
#! Using single clean() method for multiple fields 
# class Feedbackform(forms.Form):
#                 name= forms.CharField()
#                 rollno = forms.IntegerField()
#                 email = forms.EmailField()
#                 feedback = forms.CharField(widget=forms.Textarea,)

#                 def clean(self):
#                       print("Total Form Validation...")
#                       total_cleaned_data = super().clean()

#                       print("validating name")
#                       input_name  = total_cleaned_data["name"]
#                       if input_name[0].lower()!="s":
#                            raise  forms.ValidationError("The Name should be start with s")
                      

#                       print("validating rollno")
#                       input_rollno = total_cleaned_data.get('rollno')
#                       if input_rollno<=0:
#                               raise forms.ValidationError("ROLL NO SHOULBE GRATEAR THAN ZERO")
                      

#                       print("validating email ")
#                       input_email = total_cleaned_data.get("email")
#                       if input_email[-10:]!="@gmail.com":
#                               raise forms.ValidationError("The extesnional should be gmail ")


                                   
#! Matching password
class Feedbackform(forms.Form):
                name= forms.CharField()
                email = forms.EmailField()
                password = forms.CharField(label="Enter Password" ,widget= forms.PasswordInput)
                rpassword = forms.CharField(label="Password (again)", widget= forms.PasswordInput)
                feedback = forms.CharField(widget=forms.Textarea,)
                bot_handling = forms.CharField( required= False,widget=forms.HiddenInput)
#! How to prevent BOT request:


                        





                def clean(self):
                        total_cleaned_data = super().clean()

                        pwd = total_cleaned_data.get("password")
                        rpwd = total_cleaned_data.get("rpassword")

                        if pwd != rpwd :
                                raise forms.ValidationError("Password does not match - Please TrY Again : ")
                        

                        input_bot_handling = total_cleaned_data.get("bot_handling")
                        if input_bot_handling:
                                raise forms.ValidationError("Request from BOT.....can't be submitted")
                       
                        



