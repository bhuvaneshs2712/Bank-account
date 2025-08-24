from django.contrib import admin
from .models import PersonalDetails, FamilyDetails, NomineeDetails, AccountDetails

@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'account_number', 'mobile_number', 'email_id', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['first_name', 'last_name', 'account_number', 'mobile_number', 'email_id']
    readonly_fields = ['leg_number', 'account_number', 'cif_id', 'asacass_number', 'created_at', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender')
        }),
        ('Contact Information', {
            'fields': ('mobile_number', 'email_id')
        }),
        ('Address Information', {
            'fields': ('address1', 'address2', 'pincode', 'city', 'state')
        }),
        ('Identity Documents', {
            'fields': ('aadhar_number', 'pan_card_number')
        }),
        ('Bank Generated IDs', {
            'fields': ('leg_number', 'account_number', 'cif_id', 'asacass_number'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(FamilyDetails)
class FamilyDetailsAdmin(admin.ModelAdmin):
    list_display = ['personal_details', 'father_name', 'mother_name', 'emergency_contact_name']
    list_filter = ['created_at']
    search_fields = ['personal_details__first_name', 'personal_details__last_name', 'father_name', 'mother_name']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(NomineeDetails)
class NomineeDetailsAdmin(admin.ModelAdmin):
    list_display = ['personal_details', 'nominee_name', 'nominee_relation', 'nominee_mobile_number']
    list_filter = ['nominee_relation', 'created_at']
    search_fields = ['personal_details__first_name', 'personal_details__last_name', 'nominee_name']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(AccountDetails)
class AccountDetailsAdmin(admin.ModelAdmin):
    list_display = ['personal_details', 'account_type', 'scheme_type', 'deposit_amount', 'current_balance', 'is_active', 'is_approved']
    list_filter = ['account_type', 'scheme_type', 'is_active', 'is_approved', 'date_of_opening']
    search_fields = ['personal_details__first_name', 'personal_details__last_name', 'personal_details__account_number']
    readonly_fields = ['date_of_opening', 'created_at', 'updated_at']
    list_editable = ['is_active', 'is_approved']
