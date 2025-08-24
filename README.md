# SecureBank - Bank Account Management System

A comprehensive Django-based bank account management system with modern UI, animations, and full CRUD operations for managing bank accounts.

## 🏦 Features

### Core Features
- **Account Creation**: Complete 4-step account opening process
- **Personal Details**: Name, address, contact info, identity documents
- **Family Details**: Spouse, children, parents, emergency contact
- **Nominee Details**: Complete nominee information with documents
- **Account Details**: Account type, scheme, deposit amount, maturity date
- **Auto-generated IDs**: LEG number, Account number, CIF ID, ASACASS number

### Technical Features
- **Modern UI**: Bootstrap 5 with custom animations
- **Responsive Design**: Mobile-friendly interface
- **Form Validation**: Real-time client-side and server-side validation
- **Search Functionality**: Search accounts by name, number, or mobile
- **Dashboard**: Comprehensive overview with statistics
- **Admin Panel**: Full admin interface for managing accounts
- **Print Support**: Print account summaries and details

### Account Types
- **Savings Account**: High interest rates, no minimum balance
- **Current Account**: Unlimited transactions, business features
- **Fixed Deposit**: Higher interest rates, flexible tenures
- **Recurring Deposit**: Regular savings, good returns

### Scheme Types
- Regular
- Senior Citizen
- Student
- Women
- Rural

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Django 5.2.4 or higher

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bank_account_project
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Default admin credentials: admin/admin

## 📁 Project Structure

```
bank_account_project/
├── bank_system/          # Main project settings
├── accounts/            # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── forms.py         # Form classes
│   ├── urls.py          # URL patterns
│   └── admin.py         # Admin configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── accounts/        # App-specific templates
├── static/              # Static files
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
└── manage.py           # Django management script
```

## 🗄️ Database Models

### PersonalDetails
- Personal information (name, DOB, gender)
- Contact details (mobile, email)
- Address information (address1, address2, pincode, city, state)
- Identity documents (Aadhar, PAN)
- Auto-generated IDs (LEG, Account, CIF, ASACASS)

### FamilyDetails
- Spouse information (optional)
- Children details
- Parent information
- Emergency contact

### NomineeDetails
- Nominee personal information
- Contact details
- Address and identity documents

### AccountDetails
- Account type and scheme
- Opening date and maturity date
- Deposit amount and current balance
- Account status and approval status

## 🎨 UI Features

### Design Elements
- **Gradient Backgrounds**: Modern gradient color schemes
- **Card-based Layout**: Clean, organized information display
- **Animated Elements**: Smooth transitions and hover effects
- **Progress Indicators**: Visual progress steps for account creation
- **Responsive Grid**: Bootstrap grid system for all screen sizes

### Animations
- **Fade In**: Elements appear with smooth fade-in effects
- **Slide Animations**: Content slides in from left/right
- **Hover Effects**: Interactive elements with hover animations
- **Loading States**: Animated loading indicators
- **Pulse Effects**: Attention-grabbing pulse animations

### Color Scheme
- **Primary**: Blue gradient (#667eea to #764ba2)
- **Success**: Green gradient (#56ab2f to #a8e6cf)
- **Info**: Blue gradient (#4facfe to #00f2fe)
- **Warning**: Orange gradient (#ff6b6b to #ee5a24)

## 🔧 Configuration

### Settings
- **DEBUG**: True (for development)
- **Database**: SQLite (default)
- **Static Files**: Configured for development
- **Templates**: Custom template directory

### Admin Configuration
- **PersonalDetails**: Comprehensive admin interface with fieldsets
- **FamilyDetails**: Simple list display with search
- **NomineeDetails**: Organized admin view
- **AccountDetails**: Full CRUD with status management

## 📱 Usage

### Account Creation Process
1. **Personal Details**: Fill in personal information
2. **Family Details**: Add family and emergency contact
3. **Nominee Details**: Provide nominee information
4. **Account Details**: Choose account type and deposit amount
5. **Summary**: Review and confirm all details

### Dashboard Features
- **Statistics Cards**: Overview of account counts
- **Search Functionality**: Find accounts quickly
- **Account Table**: Complete list with actions
- **Quick Actions**: Common tasks and exports
- **Recent Activity**: Timeline of recent actions

### Admin Features
- **Account Management**: View, edit, and manage all accounts
- **Status Updates**: Approve/activate accounts
- **Data Export**: Export account data
- **User Management**: Manage admin users

## 🔒 Security Features

- **CSRF Protection**: Built-in Django CSRF protection
- **Form Validation**: Comprehensive input validation
- **Data Sanitization**: Clean and validate all inputs
- **Admin Authentication**: Secure admin access
- **Session Management**: Secure session handling

## 🧪 Testing

### Manual Testing Checklist
- [ ] Account creation flow
- [ ] Form validation
- [ ] Search functionality
- [ ] Admin panel access
- [ ] Responsive design
- [ ] Print functionality
- [ ] Data persistence

### Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🚀 Deployment

### Production Setup
1. Set `DEBUG = False`
2. Configure production database
3. Set up static file serving
4. Configure security settings
5. Set up web server (nginx + gunicorn)

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

## 📄 License

This project is created for educational purposes. Feel free to use and modify as needed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🎯 Future Enhancements

- [ ] Email notifications
- [ ] SMS integration
- [ ] Document upload
- [ ] Advanced reporting
- [ ] API endpoints
- [ ] Mobile app
- [ ] Multi-language support
- [ ] Advanced analytics

---

**SecureBank** - Your trusted banking partner for secure and reliable financial services. 