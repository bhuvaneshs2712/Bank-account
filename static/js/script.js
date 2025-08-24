// Bank Account Management System - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initializeAnimations();
    
    // Initialize form validations
    initializeFormValidations();
    
    // Initialize search functionality
    initializeSearch();
    
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize progress steps
    initializeProgressSteps();
});

// Animation Functions
function initializeAnimations() {
    // Add animation classes to elements when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__fadeInUp');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    document.querySelectorAll('.card, .stats-card, .hero-section').forEach(el => {
        observer.observe(el);
    });
    
    // Add hover effects to buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Form Validation Functions
function initializeFormValidations() {
    // Personal Details Form Validation
    const personalForm = document.querySelector('form');
    if (personalForm) {
        personalForm.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showNotification('Please correct the errors in the form.', 'error');
            }
        });
    }
    
    // Real-time validation for input fields
    document.querySelectorAll('input, select, textarea').forEach(field => {
        field.addEventListener('blur', function() {
            validateField(this);
        });
        
        field.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
    
    // Mobile number validation
    const mobileFields = document.querySelectorAll('input[name*="mobile"]');
    mobileFields.forEach(field => {
        field.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
            if (this.value.length > 10) {
                this.value = this.value.slice(0, 10);
            }
        });
    });
    
    // Aadhar number validation
    const aadharFields = document.querySelectorAll('input[name*="aadhar"]');
    aadharFields.forEach(field => {
        field.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
            if (this.value.length > 12) {
                this.value = this.value.slice(0, 12);
            }
        });
    });
    
    // PAN card validation
    const panFields = document.querySelectorAll('input[name*="pan"]');
    panFields.forEach(field => {
        field.addEventListener('input', function() {
            this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
            if (this.value.length > 10) {
                this.value = this.value.slice(0, 10);
            }
        });
    });
    
    // Pincode validation
    const pincodeFields = document.querySelectorAll('input[name*="pincode"]');
    pincodeFields.forEach(field => {
        field.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
            if (this.value.length > 6) {
                this.value = this.value.slice(0, 6);
            }
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    // Required field validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (fieldName.includes('email') && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Mobile number validation
    if (fieldName.includes('mobile') && value) {
        if (value.length !== 10 || !/^\d{10}$/.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid 10-digit mobile number.';
        }
    }
    
    // Aadhar number validation
    if (fieldName.includes('aadhar') && value) {
        if (value.length !== 12 || !/^\d{12}$/.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid 12-digit Aadhar number.';
        }
    }
    
    // PAN card validation
    if (fieldName.includes('pan') && value) {
        if (value.length !== 10 || !/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid PAN card number (e.g., ABCDE1234F).';
        }
    }
    
    // Pincode validation
    if (fieldName.includes('pincode') && value) {
        if (value.length !== 6 || !/^\d{6}$/.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid 6-digit pincode.';
        }
    }
    
    if (!isValid) {
        showFieldError(field, errorMessage);
    } else {
        clearFieldError(field);
    }
    
    return isValid;
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    field.classList.add('is-invalid');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

function clearFieldError(field) {
    field.classList.remove('is-invalid');
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Search Functionality
function initializeSearch() {
    const searchInput = document.querySelector('#searchInput');
    if (searchInput) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const searchTerm = this.value.trim();
            
            if (searchTerm.length >= 2) {
                searchTimeout = setTimeout(() => {
                    performSearch(searchTerm);
                }, 300);
            } else {
                clearSearchResults();
            }
        });
    }
}

function performSearch(searchTerm) {
    fetch('/search-accounts/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: `search_term=${encodeURIComponent(searchTerm)}`
    })
    .then(response => response.json())
    .then(data => {
        displaySearchResults(data.results);
    })
    .catch(error => {
        console.error('Search error:', error);
    });
}

function displaySearchResults(results) {
    const resultsContainer = document.querySelector('#searchResults');
    if (!resultsContainer) return;
    
    resultsContainer.innerHTML = '';
    
    if (results.length === 0) {
        resultsContainer.innerHTML = '<div class="p-3 text-muted">No accounts found.</div>';
        return;
    }
    
    results.forEach(result => {
        const resultItem = document.createElement('div');
        resultItem.className = 'search-result-item p-3 border-bottom';
        resultItem.innerHTML = `
            <div class="d-flex justify-content-between align-items-center">
                <div>
                    <h6 class="mb-1">${result.name}</h6>
                    <small class="text-muted">Account: ${result.account_number}</small>
                </div>
                <a href="/account-detail/${result.id}/" class="btn btn-sm btn-primary">View</a>
            </div>
        `;
        resultsContainer.appendChild(resultItem);
    });
}

function clearSearchResults() {
    const resultsContainer = document.querySelector('#searchResults');
    if (resultsContainer) {
        resultsContainer.innerHTML = '';
    }
}

// Tooltip Initialization
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Progress Steps
function initializeProgressSteps() {
    const progressSteps = document.querySelectorAll('.progress-step');
    if (progressSteps.length > 0) {
        progressSteps.forEach((step, index) => {
            step.addEventListener('click', function() {
                activateStep(index);
            });
        });
    }
}

function activateStep(stepIndex) {
    const steps = document.querySelectorAll('.progress-step');
    steps.forEach((step, index) => {
        if (index < stepIndex) {
            step.classList.add('completed');
            step.classList.remove('active');
        } else if (index === stepIndex) {
            step.classList.add('active');
            step.classList.remove('completed');
        } else {
            step.classList.remove('active', 'completed');
        }
    });
}

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Utility Functions
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Loading State Management
function showLoading(element) {
    const originalContent = element.innerHTML;
    element.innerHTML = '<span class="loading"></span> Loading...';
    element.disabled = true;
    return originalContent;
}

function hideLoading(element, originalContent) {
    element.innerHTML = originalContent;
    element.disabled = false;
}

// Form Auto-save (for long forms)
function initializeAutoSave() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const formData = new FormData(form);
        const formKey = form.action || form.id || 'form_' + Math.random();
        
        // Save form data to localStorage
        const saveFormData = () => {
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });
            localStorage.setItem(formKey, JSON.stringify(data));
        };
        
        // Load saved form data
        const loadFormData = () => {
            const saved = localStorage.getItem(formKey);
            if (saved) {
                const data = JSON.parse(saved);
                Object.keys(data).forEach(key => {
                    const field = form.querySelector(`[name="${key}"]`);
                    if (field) {
                        field.value = data[key];
                    }
                });
            }
        };
        
        // Auto-save on input
        form.addEventListener('input', saveFormData);
        
        // Load saved data on page load
        loadFormData();
        
        // Clear saved data on successful submit
        form.addEventListener('submit', () => {
            localStorage.removeItem(formKey);
        });
    });
}

// Initialize auto-save for forms
document.addEventListener('DOMContentLoaded', function() {
    initializeAutoSave();
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Print functionality for account details
function printAccountDetails() {
    window.print();
}

// Export functionality (placeholder)
function exportAccountData(format = 'pdf') {
    showNotification(`Exporting account data in ${format.toUpperCase()} format...`, 'info');
    // Implementation would depend on backend support
}

// Theme toggle (if needed)
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Load saved theme
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
}); 