# BizLoan Web Application - Complete Command Guide

## STEP 1: Project Foundation & Structure

### Command:
```
"Create a professional BizLoan web application project structure with:

Backend (Python Flask):
- Modern project structure with blueprints
- Flask-RESTful for clean API design
- MongoDB with PyMongo for data storage
- JWT authentication system
- Input validation with Marshmallow
- CORS configuration
- Error handling middleware
- Logging system
- Environment configuration

Frontend (React):
- TypeScript for better code quality
- Tailwind CSS for responsive design
- React Router for navigation
- Context API for state management
- Axios for API calls
- React Hook Form for form handling
- Professional UI components

Project Structure:
bizloan/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── utils/
│   │   ├── middleware/
│   │   └── config.py
│   ├── tests/
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   ├── types/
│   │   └── utils/
│   ├── public/
│   └── package.json
└── docker-compose.yml

Include complete setup instructions and dependency lists."
```

## STEP 2: Database Schema & Models

### Command:
```
"Design comprehensive MongoDB schemas for BizLoan application:

User Collection:
- user_id (ObjectId)
- email (unique, required)
- password (hashed)
- role ('borrower', 'lender', 'admin')
- profile: {
  - first_name, last_name
  - phone_number
  - address (street, city, state, zip)
  - date_of_birth
  - ssn (encrypted)
  - profile_image_url
  }
- verification_status ('pending', 'verified', 'rejected')
- created_at, updated_at

Business Collection:
- business_id (ObjectId)
- user_id (reference to User)
- business_info: {
  - business_name
  - legal_structure ('LLC', 'Corporation', 'Partnership', etc.)
  - industry_type
  - years_in_business
  - employee_count
  - annual_revenue
  - business_address
  - ein_number
  - business_phone
  - website_url
  }
- financial_info: {
  - monthly_revenue
  - monthly_expenses
  - credit_score
  - existing_loans
  - bank_statements (file URLs)
  - tax_returns (file URLs)
  }
- verification_documents: [file URLs]
- verification_status
- created_at, updated_at

Loan Application Collection:
- application_id (ObjectId)
- user_id (reference)
- business_id (reference)
- loan_details: {
  - loan_amount
  - loan_purpose
  - loan_term (months)
  - requested_interest_rate
  - repayment_frequency
  - collateral_offered
  }
- application_status ('draft', 'submitted', 'under_review', 'approved', 'rejected', 'funded')
- risk_assessment: {
  - credit_score_impact
  - revenue_stability_score
  - industry_risk_level
  - overall_risk_rating
  }
- documents: [file URLs]
- comments: [{
  - comment_text
  - commented_by
  - timestamp
  }]
- submitted_at, updated_at

Loan Collection (for approved loans):
- loan_id (ObjectId)
- application_id (reference)
- loan_terms: {
  - principal_amount
  - interest_rate
  - term_months
  - monthly_payment
  - total_repayment
  }
- loan_status ('active', 'paid_off', 'defaulted')
- payment_schedule: [{
  - payment_number
  - due_date
  - amount_due
  - principal_portion
  - interest_portion
  - status ('pending', 'paid', 'late', 'missed')
  }]
- disbursement_date
- created_at

Include MongoDB connection utilities, model validation functions, and sample data scripts."
```

## STEP 3: Authentication & User Management

### Command:
```
"Create secure authentication system for BizLoan application:

Authentication Endpoints:
POST /api/auth/register
- Fields: email, password, confirm_password, role, first_name, last_name
- Validation: email format, password strength (8+ chars, special chars), unique email
- Password hashing with bcrypt
- Send email verification link
- Return: user info (no password), verification status

POST /api/auth/verify-email
- Accept: verification_token
- Update user verification status
- Return: success message

POST /api/auth/login
- Fields: email, password
- Validate credentials
- Generate JWT with user role and permissions
- Return: JWT token, user info, expires_in

POST /api/auth/forgot-password
- Accept: email
- Generate reset token
- Send reset email
- Return: success message

POST /api/auth/reset-password
- Accept: reset_token, new_password, confirm_password
- Validate token and update password
- Return: success message

Protected Routes:
GET /api/auth/profile (JWT required)
PUT /api/auth/profile (JWT required)
POST /api/auth/change-password (JWT required)
POST /api/auth/logout (JWT required)

Security Features:
- JWT middleware with role-based access
- Rate limiting for auth endpoints
- Account lockout after failed attempts
- Password strength validation
- Email verification requirement
- Two-factor authentication option
- Session management
- Security headers

Include complete error handling and input validation."
```

## STEP 4: Business Profile Management

### Command:
```
"Create business profile management system:

Business Profile Endpoints:
POST /api/business/profile (Protected - Borrower only)
- Accept all business information fields
- File upload for business documents
- Validation for EIN format, revenue figures
- Create business profile linked to user
- Return: business profile data

GET /api/business/profile (Protected)
- Return: user's business profile
- Include document URLs and verification status

PUT /api/business/profile (Protected)
- Update business information
- Handle document uploads/updates
- Re-trigger verification if needed
- Return: updated profile

POST /api/business/upload-documents (Protected)
- Handle multiple file uploads
- Validate file types (PDF, JPG, PNG)
- Secure file storage with unique names
- Update business profile with document URLs
- Return: uploaded file info

GET /api/business/verification-status (Protected)
- Return: current verification status and requirements
- List missing documents or information

Document Types Supported:
- Business license
- Tax returns (last 2 years)
- Bank statements (last 6 months)
- Financial statements
- Proof of address
- Articles of incorporation

Features:
- File size validation (max 10MB per file)
- Virus scanning for uploads
- Secure file storage with access controls
- Document preview functionality
- Verification workflow integration
- Progress tracking for profile completion

Include complete file handling utilities and validation."
```

## STEP 5: Loan Application System

### Command:
```
"Create comprehensive loan application system:

Loan Application Endpoints:
POST /api/loans/applications (Protected - Borrower)
- Accept: loan_amount, loan_purpose, loan_term, requested_rate, collateral_details
- Validation: amount limits, term ranges, purpose categories
- Create draft application
- Return: application_id and status

PUT /api/loans/applications/:id (Protected - Owner only)
- Update draft application
- Validate all inputs
- Return: updated application

POST /api/loans/applications/:id/submit (Protected - Owner only)
- Submit application for review
- Validate all required fields and documents
- Trigger risk assessment
- Send notification to admins
- Update status to 'submitted'
- Return: submission confirmation

GET /api/loans/applications (Protected)
- For borrowers: return their applications
- For admins: return all applications with filters
- Include pagination, sorting, filtering
- Return: applications list with status

GET /api/loans/applications/:id (Protected)
- Return: detailed application info
- Include business profile and documents
- Show risk assessment if available
- Include comment history

POST /api/loans/applications/:id/comments (Protected - Admin only)
- Add comments to application
- Notify applicant of new comments
- Return: updated comments list

Risk Assessment Features:
- Automatic credit score evaluation
- Revenue stability analysis
- Industry risk assessment
- Debt-to-income ratio calculation
- Overall risk rating generation

Loan Purposes:
- Working capital
- Equipment purchase
- Inventory financing
- Real estate
- Business expansion
- Debt consolidation
- Marketing/advertising
- Other (specify)

Include complete validation, risk assessment algorithms, and notification system."
```

## STEP 6: Admin Dashboard & Loan Management

### Command:
```
"Create admin dashboard for loan management:

Admin Endpoints:
GET /api/admin/dashboard (Protected - Admin only)
- Return: dashboard statistics
  - Total applications (by status)
  - Total loan amounts
  - Default rates
  - Recent activity
  - Monthly/yearly trends

GET /api/admin/applications (Protected - Admin only)
- Return: all applications with advanced filtering
- Filters: status, date range, loan amount, risk level
- Sorting: date, amount, risk score
- Pagination with search
- Export to CSV functionality

PUT /api/admin/applications/:id/status (Protected - Admin only)
- Update application status
- Accept: new_status, comments, terms (if approved)
- Send notifications to applicant
- If approved, create loan record
- Return: updated application

POST /api/admin/applications/:id/approve (Protected - Admin only)
- Approve loan application
- Accept: final_amount, interest_rate, term, conditions
- Generate loan agreement
- Create payment schedule
- Send approval notification
- Return: loan details

POST /api/admin/applications/:id/reject (Protected - Admin only)
- Reject application with reason
- Accept: rejection_reason, feedback
- Send rejection email
- Return: confirmation

GET /api/admin/users (Protected - Admin only)
- Return: all users with filtering
- Include verification status
- User activity metrics
- Account management options

POST /api/admin/users/:id/verify (Protected - Admin only)
- Verify user account manually
- Update verification status
- Send confirmation email
- Return: updated user status

Loan Management:
GET /api/admin/loans (Protected - Admin only)
- Return: all active loans
- Include payment status and history
- Default tracking
- Performance metrics

PUT /api/admin/loans/:id/payment (Protected - Admin only)
- Record loan payment
- Update payment schedule
- Calculate remaining balance
- Send payment confirmation
- Return: updated loan status

Admin Analytics:
- Loan approval rates
- Default predictions
- Portfolio performance
- Risk distribution
- Revenue analytics

Include complete admin interface with role-based permissions."
```

## STEP 7: Frontend - Authentication & Layout

### Command:
```
"Create professional React frontend for BizLoan application:

Authentication Components:
- LoginForm with email/password validation
- RegisterForm with role selection
- ForgotPasswordForm with email input
- ResetPasswordForm with token validation
- EmailVerificationPage
- Two-factor authentication component

Layout Components:
- Header with navigation and user menu
- Sidebar with role-based menu items
- Footer with company info and links
- LoadingSpinner an