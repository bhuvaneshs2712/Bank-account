from django.db import models
import uuid
from datetime import datetime, timedelta

class PersonalDetails(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])
    
    # Contact Information
    mobile_number = models.CharField(max_length=15, unique=True)
    email_id = models.EmailField(unique=True)
    
    # Address Information
    address1 = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    # Identity Documents
    aadhar_number = models.CharField(max_length=12, unique=True)
    pan_card_number = models.CharField(max_length=10, unique=True)
    
    # Bank Generated IDs
    leg_number = models.CharField(max_length=20, unique=True, blank=True)
    account_number = models.CharField(max_length=20, unique=True, blank=True)
    cif_id = models.CharField(max_length=20, unique=True, blank=True)
    asacass_number = models.CharField(max_length=20, unique=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.leg_number:
            self.leg_number = f"LEG{str(uuid.uuid4())[:8].upper()}"
        if not self.account_number:
            self.account_number = f"ACC{str(uuid.uuid4())[:12].upper()}"
        if not self.cif_id:
            self.cif_id = f"CIF{str(uuid.uuid4())[:10].upper()}"
        if not self.asacass_number:
            self.asacass_number = f"ASA{str(uuid.uuid4())[:15].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.account_number}"
    
    class Meta:
        verbose_name_plural = "Personal Details"

class FamilyDetails(models.Model):
    personal_details = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name='family_details')
    
    # Spouse Information
    spouse_name = models.CharField(max_length=200, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    
    # Children Information
    children_count = models.PositiveIntegerField(default=0)
    children_details = models.TextField(blank=True, null=True)
    
    # Parent Information
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_relation = models.CharField(max_length=50)
    emergency_contact_mobile = models.CharField(max_length=15)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Family Details - {self.personal_details.first_name} {self.personal_details.last_name}"
    
    class Meta:
        verbose_name_plural = "Family Details"

class NomineeDetails(models.Model):
    personal_details = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name='nominee_details')
    
    nominee_name = models.CharField(max_length=200)
    nominee_relation = models.CharField(max_length=50)
    nominee_date_of_birth = models.DateField()
    nominee_mobile_number = models.CharField(max_length=15)
    nominee_email = models.EmailField(blank=True, null=True)
    nominee_address = models.TextField()
    nominee_aadhar_number = models.CharField(max_length=12)
    nominee_pan_card_number = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Nominee - {self.nominee_name} for {self.personal_details.first_name} {self.personal_details.last_name}"
    
    class Meta:
        verbose_name_plural = "Nominee Details"

class AccountDetails(models.Model):
    ACCOUNT_TYPES = [
        ('SAVINGS', 'Savings Account'),
        ('CURRENT', 'Current Account'),
        ('FIXED_DEPOSIT', 'Fixed Deposit'),
        ('RECURRING_DEPOSIT', 'Recurring Deposit'),
    ]
    
    SCHEME_TYPES = [
        ('REGULAR', 'Regular'),
        ('SENIOR_CITIZEN', 'Senior Citizen'),
        ('STUDENT', 'Student'),
        ('WOMEN', 'Women'),
        ('RURAL', 'Rural'),
    ]
    
    personal_details = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE, related_name='account_details')
    
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    scheme_type = models.CharField(max_length=20, choices=SCHEME_TYPES)
    
    # Account Information
    date_of_opening = models.DateField(auto_now_add=True)
    maturity_date = models.DateField(blank=True, null=True)
    deposit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    
    # Account Status
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    
    # Additional Details
    branch_code = models.CharField(max_length=10, default='MAIN001')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=3.50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.account_type in ['FIXED_DEPOSIT', 'RECURRING_DEPOSIT'] and not self.maturity_date:
            # Set maturity date to 1 year from opening for fixed deposits
            self.maturity_date = self.date_of_opening + timedelta(days=365)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.account_type} - {self.personal_details.account_number}"
    
    class Meta:
        verbose_name_plural = "Account Details"
