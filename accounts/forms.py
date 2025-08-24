from django import forms
from .models import PersonalDetails, FamilyDetails, NomineeDetails, AccountDetails

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'mobile_number', 'email_id', 'address1', 'address2',
            'pincode', 'city', 'state', 'aadhar_number', 'pan_card_number'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'address1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Address Line 1'}),
            'address2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Address Line 2 (Optional)'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pincode'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhar Number'}),
            'pan_card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PAN Card Number'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

class FamilyDetailsForm(forms.ModelForm):
    class Meta:
        model = FamilyDetails
        fields = [
            'spouse_name', 'spouse_occupation', 'children_count', 'children_details',
            'father_name', 'mother_name', 'emergency_contact_name',
            'emergency_contact_relation', 'emergency_contact_mobile'
        ]
        widgets = {
            'spouse_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Spouse Name (Optional)'}),
            'spouse_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Spouse Occupation (Optional)'}),
            'children_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'children_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Children Details (Optional)'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mother Name'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Emergency Contact Name'}),
            'emergency_contact_relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Relation with Emergency Contact'}),
            'emergency_contact_mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Emergency Contact Mobile'}),
        }

class NomineeDetailsForm(forms.ModelForm):
    class Meta:
        model = NomineeDetails
        fields = [
            'nominee_name', 'nominee_relation', 'nominee_date_of_birth',
            'nominee_mobile_number', 'nominee_email', 'nominee_address',
            'nominee_aadhar_number', 'nominee_pan_card_number'
        ]
        widgets = {
            'nominee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nominee Name'}),
            'nominee_relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Relation with Nominee'}),
            'nominee_date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nominee_mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nominee Mobile Number'}),
            'nominee_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nominee Email (Optional)'}),
            'nominee_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Nominee Address'}),
            'nominee_aadhar_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nominee Aadhar Number'}),
            'nominee_pan_card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nominee PAN Card Number'}),
        }

class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = AccountDetails
        fields = ['account_type', 'scheme_type', 'deposit_amount']
        widgets = {
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'scheme_type': forms.Select(attrs={'class': 'form-control'}),
            'deposit_amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 0.01, 'placeholder': 'Enter Deposit Amount'}),
        } 