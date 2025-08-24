from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import PersonalDetails, FamilyDetails, NomineeDetails, AccountDetails
from .forms import PersonalDetailsForm, FamilyDetailsForm, NomineeDetailsForm, AccountDetailsForm
from django.db import models

def home(request):
    """Home page view"""
    return render(request, 'accounts/home.html')

def personal_details(request):
    """Personal details form view"""
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            personal_detail = form.save()
            messages.success(request, 'Personal details saved successfully!')
            return redirect('family_details', personal_id=personal_detail.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PersonalDetailsForm()
    
    return render(request, 'accounts/personal_details.html', {'form': form})

def family_details(request, personal_id):
    """Family details form view"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    if request.method == 'POST':
        form = FamilyDetailsForm(request.POST)
        if form.is_valid():
            family_detail = form.save(commit=False)
            family_detail.personal_details = personal_detail
            family_detail.save()
            messages.success(request, 'Family details saved successfully!')
            return redirect('nominee_details', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FamilyDetailsForm()
    
    return render(request, 'accounts/family_details.html', {
        'form': form,
        'personal_detail': personal_detail
    })

def nominee_details(request, personal_id):
    """Nominee details form view"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    if request.method == 'POST':
        form = NomineeDetailsForm(request.POST)
        if form.is_valid():
            nominee_detail = form.save(commit=False)
            nominee_detail.personal_details = personal_detail
            nominee_detail.save()
            messages.success(request, 'Nominee details saved successfully!')
            return redirect('account_details', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = NomineeDetailsForm()
    
    return render(request, 'accounts/nominee_details.html', {
        'form': form,
        'personal_detail': personal_detail
    })

def account_details(request, personal_id):
    """Account details form view"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    if request.method == 'POST':
        form = AccountDetailsForm(request.POST)
        if form.is_valid():
            account_detail = form.save(commit=False)
            account_detail.personal_details = personal_detail
            account_detail.current_balance = account_detail.deposit_amount
            account_detail.save()
            messages.success(request, 'Account details saved successfully!')
            return redirect('account_summary', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AccountDetailsForm()
    
    return render(request, 'accounts/account_details.html', {
        'form': form,
        'personal_detail': personal_detail
    })

def account_summary(request, personal_id):
    """Account summary view"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    try:
        family_detail = personal_detail.family_details
    except FamilyDetails.DoesNotExist:
        family_detail = None
    
    try:
        nominee_detail = personal_detail.nominee_details
    except NomineeDetails.DoesNotExist:
        nominee_detail = None
    
    try:
        account_detail = personal_detail.account_details
    except AccountDetails.DoesNotExist:
        account_detail = None
    
    return render(request, 'accounts/account_summary.html', {
        'personal_detail': personal_detail,
        'family_detail': family_detail,
        'nominee_detail': nominee_detail,
        'account_detail': account_detail
    })

def dashboard(request):
    """Dashboard view showing all accounts"""
    accounts = PersonalDetails.objects.all().order_by('-created_at')
    return render(request, 'accounts/dashboard.html', {'accounts': accounts})

def account_detail_view(request, personal_id):
    """Detailed view of a specific account"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    try:
        family_detail = personal_detail.family_details
    except FamilyDetails.DoesNotExist:
        family_detail = None
    
    try:
        nominee_detail = personal_detail.nominee_details
    except NomineeDetails.DoesNotExist:
        nominee_detail = None
    
    try:
        account_detail = personal_detail.account_details
    except AccountDetails.DoesNotExist:
        account_detail = None
    
    return render(request, 'accounts/account_detail.html', {
        'personal_detail': personal_detail,
        'family_detail': family_detail,
        'nominee_detail': nominee_detail,
        'account_detail': account_detail
    })

def edit_personal_details(request, personal_id):
    """Edit personal details"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal details updated successfully!')
            return redirect('account_detail_view', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PersonalDetailsForm(instance=personal_detail)
    
    return render(request, 'accounts/edit_personal_details.html', {
        'form': form,
        'personal_detail': personal_detail
    })

def edit_family_details(request, personal_id):
    """Edit family details"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    try:
        family_detail = personal_detail.family_details
    except FamilyDetails.DoesNotExist:
        family_detail = None
    
    if request.method == 'POST':
        if family_detail:
            form = FamilyDetailsForm(request.POST, instance=family_detail)
        else:
            form = FamilyDetailsForm(request.POST)
        
        if form.is_valid():
            family_detail = form.save(commit=False)
            family_detail.personal_details = personal_detail
            family_detail.save()
            messages.success(request, 'Family details updated successfully!')
            return redirect('account_detail_view', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        if family_detail:
            form = FamilyDetailsForm(instance=family_detail)
        else:
            form = FamilyDetailsForm()
    
    return render(request, 'accounts/edit_family_details.html', {
        'form': form,
        'personal_detail': personal_detail,
        'family_detail': family_detail
    })

def edit_nominee_details(request, personal_id):
    """Edit nominee details"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    try:
        nominee_detail = personal_detail.nominee_details
    except NomineeDetails.DoesNotExist:
        nominee_detail = None
    
    if request.method == 'POST':
        if nominee_detail:
            form = NomineeDetailsForm(request.POST, instance=nominee_detail)
        else:
            form = NomineeDetailsForm(request.POST)
        
        if form.is_valid():
            nominee_detail = form.save(commit=False)
            nominee_detail.personal_details = personal_detail
            nominee_detail.save()
            messages.success(request, 'Nominee details updated successfully!')
            return redirect('account_detail_view', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        if nominee_detail:
            form = NomineeDetailsForm(instance=nominee_detail)
        else:
            form = NomineeDetailsForm()
    
    return render(request, 'accounts/edit_nominee_details.html', {
        'form': form,
        'personal_detail': personal_detail,
        'nominee_detail': nominee_detail
    })

def edit_account_details(request, personal_id):
    """Edit account details"""
    personal_detail = get_object_or_404(PersonalDetails, id=personal_id)
    
    try:
        account_detail = personal_detail.account_details
    except AccountDetails.DoesNotExist:
        account_detail = None
    
    if request.method == 'POST':
        if account_detail:
            form = AccountDetailsForm(request.POST, instance=account_detail)
        else:
            form = AccountDetailsForm(request.POST)
        
        if form.is_valid():
            account_detail = form.save(commit=False)
            account_detail.personal_details = personal_detail
            if not account_detail.current_balance:
                account_detail.current_balance = account_detail.deposit_amount
            account_detail.save()
            messages.success(request, 'Account details updated successfully!')
            return redirect('account_detail_view', personal_id=personal_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        if account_detail:
            form = AccountDetailsForm(instance=account_detail)
        else:
            form = AccountDetailsForm()
    
    return render(request, 'accounts/edit_account_details.html', {
        'form': form,
        'personal_detail': personal_detail,
        'account_detail': account_detail
    })

@csrf_exempt
def search_accounts(request):
    """Search accounts by account number or name"""
    if request.method == 'POST':
        search_term = request.POST.get('search_term', '')
        accounts = PersonalDetails.objects.filter(
            models.Q(account_number__icontains=search_term) |
            models.Q(first_name__icontains=search_term) |
            models.Q(last_name__icontains=search_term)
        )[:10]
        
        results = []
        for account in accounts:
            results.append({
                'id': account.id,
                'name': f"{account.first_name} {account.last_name}",
                'account_number': account.account_number,
                'mobile': account.mobile_number
            })
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'results': []})
