from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_mail import Mail, Message
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
from config import get_config
from language import language_selector_middleware, register_template_functions
from email_utils import send_contact_email

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get configuration
config = get_config()

app = Flask(__name__)
app.config.from_object(config)

# Initialize Flask-Mail
mail = Mail(app)

# Register middleware and template functions
app.before_request(language_selector_middleware)
register_template_functions(app)

@app.route('/')
def index():
    """Render the homepage"""
    return render_template('index.html', active_page='home')

@app.route('/pages/laos')
def laos_page():
    """Render the Laos page"""
    return render_template('pages/laos.html', active_page='laos')

@app.route('/pages/vietnam')
def vietnam_page():
    """Render the Vietnam page"""
    return render_template('pages/vietnam.html', active_page='vietnamese')

@app.route('/pages/thailand') 
def thailand_page():
    """Render the Thailand page"""
    return render_template('pages/thailand.html', active_page='thai')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle the contact form page and form submission"""
    if request.method == 'POST':
        # Get form data
        form_data = {
            'title': request.form.get('title'),
            'company': request.form.get('company'),
            'website': request.form.get('website'),
            'address': request.form.get('address'),
            'name': request.form.get('name'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'business': request.form.get('business'),
            'message': request.form.get('message')
        }
        
        # Validate required fields
        required_fields = [
            ('title', 'field_title'),
            ('company', 'field_company'),
            ('address', 'field_address'),
            ('name', 'field_name'),
            ('phone', 'field_phone'),
            ('email', 'field_email'),
            ('message', 'field_message')
        ]
        
        missing_fields = []
        for field, label in required_fields:
            if not form_data.get(field):
                from language import translate
                missing_fields.append(translate(label))
        
        if missing_fields:
            from language import translate
            flash(translate('required_fields', ', '.join(missing_fields)), 'error')
            return render_template('contact.html', active_page='contact', form_data=form_data)
            
        # Send the email
        success, message = send_contact_email(mail, app.config, form_data)
        
        if success:
            # Redirect to thank you page
            from language import translate
            flash(translate('email_success'), 'success')
            return redirect(url_for('thank_you'))
        else:
            # Show error message
            from language import translate
            flash(translate('email_error') + f": {message}", 'error')
            
    return render_template('contact.html', active_page='contact', form_data={})

@app.route('/thank-you')
def thank_you():
    """Render the thank you page after form submission"""
    return render_template('thank_you.html')

@app.route('/change-language/<lang_code>')
def change_language(lang_code):
    """Change the language and redirect back to the previous page"""
    from language import LANGUAGES
    
    # Only set if it's a valid language
    if lang_code in LANGUAGES:
        from flask import session
        session['lang'] = lang_code
    
    # Redirect back to the referring page or home
    referrer = request.referrer
    if referrer:
        return redirect(referrer)
    else:
        return redirect(url_for('index'))

# Serve static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    logger.error(f"500 error: {str(e)}")
    return render_template('500.html'), 500

@app.context_processor
def inject_now():
    """Inject current date into templates"""
    return {'now': datetime.utcnow}

# Run the application
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))