from flask import Flask, render_template, request, jsonify, session
import smtplib
import requests
import json
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sqlite3
import os
from werkzeug.security import generate_password_hash
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BizloanChatbot:
    def __init__(self):
        self.loan_types = {
            'business_loan': {
                'name': 'Business Loan',
                'interest_rate': '10.5% - 18%',
                'max_amount': '₹5 Crores',
                'tenure': '1-5 years'
            },
            'personal_loan': {
                'name': 'Personal Loan',
                'interest_rate': '12% - 24%',
                'max_amount': '₹40 Lakhs',
                'tenure': '1-7 years'
            },
            'home_loan': {
                'name': 'Home Loan',
                'interest_rate': '8.5% - 12%',
                'max_amount': '₹10 Crores',
                'tenure': '10-30 years'
            },
            'msme_loan': {
                'name': 'MSME Loan',
                'interest_rate': '9.5% - 16%',
                'max_amount': '₹2 Crores',
                'tenure': '1-7 years'
            }
        }
        
        self.female_responses = [
            "I'd be happy to help you with that! 😊",
            "Let me assist you with your loan inquiry! 💼",
            "I'm here to guide you through your business loan journey! ✨",
            "That's a great question! Let me provide you with the details! 🌟",
            "I understand your concern, let me help clarify that for you! 💫"
        ]
        
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for storing inquiries"""
        conn = sqlite3.connect('bizloan.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                loan_type TEXT,
                amount TEXT,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_inquiry(self, data):
        """Save user inquiry to database"""
        conn = sqlite3.connect('bizloan.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO inquiries (name, email, phone, loan_type, amount, message)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data.get('name'), data.get('email'), data.get('phone'), 
              data.get('loan_type'), data.get('amount'), data.get('message')))
        
        conn.commit()
        conn.close()
    
    def get_loan_eligibility(self, income, loan_amount, credit_score=750):
        """Calculate loan eligibility using a mock API simulation"""
        try:
            # Mock eligibility calculation
            income = float(income.replace(',', '').replace('₹', ''))
            amount = float(loan_amount.replace(',', '').replace('₹', ''))
            
            max_eligible = income * 60  # 60x monthly income
            
            if amount <= max_eligible and credit_score >= 650:
                approval_chance = min(95, (credit_score / 850) * 100)
                return {
                    'eligible': True,
                    'max_amount': f"₹{max_eligible:,.0f}",
                    'approval_chance': f"{approval_chance:.0f}%",
                    'recommended_tenure': '3-5 years'
                }
            else:
                return {
                    'eligible': False,
                    'reason': 'Income or credit score does not meet minimum requirements',
                    'suggestions': 'Consider improving credit score or reducing loan amount'
                }
        except:
            return {'error': 'Invalid input format'}
    
    def get_interest_rates(self):
        """Fetch current interest rates (mock API)"""
        return {
            'personal_loan': {'min': 12.0, 'max': 24.0},
            'business_loan': {'min': 10.5, 'max': 18.0},
            'home_loan': {'min': 8.5, 'max': 12.0},
            'msme_loan': {'min': 9.5, 'max': 16.0}
        }
    
    def send_email(self, to_email, subject, message):
        """Send email notification"""
        try:
            # Configure your SMTP settings
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "your-email@gmail.com"  # Replace with your email
            sender_password = "your-app-password"  # Use app password for Gmail
            
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'html'))
            
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)
            server.quit()
            
            return True
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}")
            return False
    
    def process_query(self, user_message, user_data=None):
        """Process user query and return appropriate response"""
        message = user_message.lower()
        
        # Greeting responses
        if any(word in message for word in ['hello', 'hi', 'hey', 'namaste']):
            return {
                'response': f"{random.choice(self.female_responses)} I'm Priya, your virtual loan assistant from Bizloan India. How can I help you today?",
                'type': 'greeting'
            }
        
        # Loan types inquiry
        elif any(word in message for word in ['loan types', 'what loans', 'types of loan']):
            response = "Here are the loan types we offer:\n\n"
            for key, loan in self.loan_types.items():
                response += f"🏦 **{loan['name']}**\n"
                response += f"   • Interest Rate: {loan['interest_rate']}\n"
                response += f"   • Max Amount: {loan['max_amount']}\n"
                response += f"   • Tenure: {loan['tenure']}\n\n"
            
            return {
                'response': response,
                'type': 'loan_info',
                'data': self.loan_types
            }
        
        # Interest rates
        elif any(word in message for word in ['interest rate', 'rates', 'roi']):
            rates = self.get_interest_rates()
            response = "Current Interest Rates:\n\n"
            for loan_type, rate in rates.items():
                response += f"📈 {loan_type.replace('_', ' ').title()}: {rate['min']}% - {rate['max']}%\n"
            
            return {
                'response': response,
                'type': 'rates',
                'data': rates
            }
        
        # Eligibility check
        elif any(word in message for word in ['eligible', 'eligibility', 'qualify']):
            return {
                'response': "To check your loan eligibility, I'll need some information. Please share:\n\n• Monthly Income\n• Desired Loan Amount\n• Employment Type (Salaried/Self-employed)\n\nOr you can fill out our quick eligibility form!",
                'type': 'eligibility_request'
            }
        
        # Documents required
        elif any(word in message for word in ['documents', 'papers', 'requirements']):
            return {
                'response': """Here are the typical documents required:
                
📋 **For Salaried Individuals:**
• Salary slips (last 3 months)
• Bank statements (last 6 months)
• PAN card & Aadhaar card
• Form 16 or ITR
• Employment letter

📋 **For Self-Employed:**
• ITR for last 2 years
• Business registration certificate
• Bank statements (last 12 months)
• PAN card & Aadhaar card
• GST registration (if applicable)""",
                'type': 'documents'
            }
        
        # Application process
        elif any(word in message for word in ['apply', 'application', 'process']):
            return {
                'response': """Our Simple Application Process:
                
✅ **Step 1:** Fill online application form
✅ **Step 2:** Upload required documents
✅ **Step 3:** Our team reviews your application
✅ **Step 4:** Get approval within 24-48 hours
✅ **Step 5:** Amount disbursed to your account

Would you like me to help you start an application?""",
                'type': 'process'
            }
        
        # Contact information
        elif any(word in message for word in ['contact', 'phone', 'call', 'speak']):
            return {
                'response': """📞 **Contact Bizloan India:**
                
• **Phone:** 1800-123-4567 (Toll Free)
• **WhatsApp:** +91-9876543210
• **Email:** support@bizloanindia.com
• **Office Hours:** Mon-Sat, 9 AM - 7 PM

You can also schedule a callback, and our expert will call you within 30 minutes!""",
                'type': 'contact'
            }
        
        # Default response
        else:
            return {
                'response': f"{random.choice(self.female_responses)} I can help you with loan information, eligibility checks, interest rates, required documents, and application process. What would you like to know more about?",
                'type': 'default'
            }

# Initialize chatbot
chatbot = BizloanChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    user_data = request.json.get('user_data', {})
    
    response = chatbot.process_query(user_message, user_data)
    return jsonify(response)

@app.route('/eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    income = data.get('income', '')
    loan_amount = data.get('amount', '')
    
    result = chatbot.get_loan_eligibility(income, loan_amount)
    return jsonify(result)

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    data = request.json
    
    # Save to database
    chatbot.save_inquiry(data)
    
    # Send email notification
    email_subject = "New Loan Inquiry - Bizloan India"
    email_message = f"""
    <h2>New Loan Inquiry Received</h2>
    <p><strong>Name:</strong> {data.get('name')}</p>
    <p><strong>Email:</strong> {data.get('email')}</p>
    <p><strong>Phone:</strong> {data.get('phone')}</p>
    <p><strong>Loan Type:</strong> {data.get('loan_type')}</p>
    <p><strong>Amount:</strong> {data.get('amount')}</p>
    <p><strong>Message:</strong> {data.get('message')}</p>
    <p><strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    """
    
    # Send confirmation email to user
    user_email_subject = "Thank You for Your Inquiry - Bizloan India"
    user_email_message = f"""
    <h2>Thank You, {data.get('name')}!</h2>
    <p>We have received your loan inquiry and our team will contact you within 24 hours.</p>
    <p><strong>Your Inquiry Details:</strong></p>
    <ul>
        <li>Loan Type: {data.get('loan_type')}</li>
        <li>Amount: {data.get('amount')}</li>
    </ul>
    <p>Best regards,<br>Team Bizloan India</p>
    """
    
    email_sent = chatbot.send_email(data.get('email'), user_email_subject, user_email_message)
    
    return jsonify({
        'success': True,
        'message': 'Your inquiry has been submitted successfully!',
        'email_sent': email_sent
    })

@app.route('/callback', methods=['POST'])
def request_callback():
    data = request.json
    # In a real application, you would integrate with a callback system
    return jsonify({
        'success': True,
        'message': f"Callback requested for {data.get('phone')}. Our team will call you within 30 minutes!"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)