"""
Email utilities for Kingdom Foods website.
Handles email sending and templating for the contact form.
"""

import logging
from flask import render_template
from flask_mail import Message
from datetime import datetime

# Set up logging
logger = logging.getLogger(__name__)

def send_contact_email(mail, config, form_data):
    """
    Send contact form email to the admin
    
    Args:
        mail: Flask-Mail instance
        config: Application config
        form_data: Contact form data dictionary
        
    Returns:
        (bool, str): Tuple of (success, message)
    """
    try:
        # Create and send email to admin
        email_body = render_admin_email_body(form_data)
        
        # Log the recipient email for debugging
        logger.info(f"Sending admin notification to: {config['CONTACT_EMAIL']}")
        
        admin_msg = Message(
            subject=f"Contact from Kingdom Foods Website: {form_data.get('title', 'No Title')}",
            recipients=[config['CONTACT_EMAIL']],
            html=email_body,
            sender=config['MAIL_DEFAULT_SENDER']
        )
        mail.send(admin_msg)
        logger.info("Admin notification email sent successfully")
        
        # Send confirmation email to the user
        send_confirmation_email(mail, config, form_data)
        
        return True, "Your message has been sent successfully. Thank you for contacting us!"
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        # More detailed error for debugging
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False, f"An error occurred while sending the email: {str(e)}"

def send_confirmation_email(mail, config, form_data):
    """
    Send confirmation email to the user
    
    Args:
        mail: Flask-Mail instance
        config: Application config
        form_data: Contact form data dictionary
    """
    try:
        email = form_data.get('email')
        name = form_data.get('name')
        
        # Only send if we have a valid email
        if not email:
            logger.warning("No email provided for confirmation email")
            return
        
        logger.info(f"Sending confirmation email to: {email}")
        
        confirmation_body = render_confirmation_email_body(form_data)
        
        msg = Message(
            subject="Thank you for contacting Kingdom Foods",
            recipients=[email],
            html=confirmation_body,
            sender=config['MAIL_DEFAULT_SENDER']
        )
        mail.send(msg)
        logger.info(f"Confirmation email sent successfully to: {email}")
    except Exception as e:
        # Log but don't fail the whole process if confirmation email fails
        logger.error(f"Error sending confirmation email: {str(e)}")
        import traceback
        logger.error(f"Confirmation email traceback: {traceback.format_exc()}")

def render_admin_email_body(form_data):
    """
    Render the HTML email body for admin notification
    
    Args:
        form_data: Contact form data dictionary
        
    Returns:
        str: HTML email content
    """
    # Format current date and time
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    email_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .email-container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            h2 {{ color: #C3753B; border-bottom: 2px solid #C3753B; padding-bottom: 10px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            table, th, td {{ border: 1px solid #ddd; }}
            th, td {{ padding: 12px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            .footer {{ margin-top: 30px; font-size: 0.9em; color: #777; border-top: 1px solid #ddd; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <h2>New Contact Form Submission from Kingdom Foods Website</h2>
            <p>A new contact form submission was received on {current_time}</p>
            
            <table>
                <tr>
                    <th>Field</th>
                    <th>Information</th>
                </tr>
                <tr>
                    <td><strong>Title:</strong></td>
                    <td>{form_data.get('title', '')}</td>
                </tr>
                <tr>
                    <td><strong>Company:</strong></td>
                    <td>{form_data.get('company', '')}</td>
                </tr>
                <tr>
                    <td><strong>Website:</strong></td>
                    <td>{form_data.get('website', '')}</td>
                </tr>
                <tr>
                    <td><strong>Address:</strong></td>
                    <td>{form_data.get('address', '')}</td>
                </tr>
                <tr>
                    <td><strong>Name:</strong></td>
                    <td>{form_data.get('name', '')}</td>
                </tr>
                <tr>
                    <td><strong>Phone:</strong></td>
                    <td>{form_data.get('phone', '')}</td>
                </tr>
                <tr>
                    <td><strong>Email:</strong></td>
                    <td>{form_data.get('email', '')}</td>
                </tr>
                <tr>
                    <td><strong>Business Model:</strong></td>
                    <td>{form_data.get('business', '')}</td>
                </tr>
                <tr>
                    <td><strong>Message:</strong></td>
                    <td>{form_data.get('message', '').replace('\\n', '<br>')}</td>
                </tr>
            </table>
            
            <div class="footer">
                <p>This is an automated message from the Kingdom Foods website.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return email_body

def render_confirmation_email_body(form_data):
    """
    Render the HTML email body for user confirmation
    
    Args:
        form_data: Contact form data dictionary
        
    Returns:
        str: HTML email content
    """
    name = form_data.get('name', 'Valued Customer')
    current_date = datetime.utcnow().strftime("%Y-%m-%d")
    
    email_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .email-container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            h2 {{ color: #C3753B; border-bottom: 2px solid #C3753B; padding-bottom: 10px; }}
            .message-box {{ background-color: #f9f9f9; padding: 15px; border-left: 4px solid #C3753B; margin: 20px 0; }}
            .footer {{ margin-top: 30px; font-size: 0.9em; color: #777; border-top: 1px solid #ddd; padding-top: 10px; }}
            .contact-info {{ margin-top: 30px; }}
            .contact-info p {{ margin: 5px 0; }}
            .logo {{ text-align: center; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="email-container">
            
            <h2>Thank You for Contacting Kingdom Foods</h2>
            
            <p>Dear {name},</p>
            
            <p>Thank you for reaching out to Kingdom Foods. We have received your inquiry and our team will review it promptly.</p>
            
            <div class="message-box">
                <p><strong>Inquiry Subject:</strong> {form_data.get('title', 'General Inquiry')}</p>
                <p><strong>Date Received:</strong> {current_date}</p>
            </div>
            
            <p>We typically respond to inquiries within 1-2 business days. If your matter is urgent, please feel free to contact us directly using the information below.</p>
            
            <div class="contact-info">
                <p><strong>Email:</strong> info@kf-asia.com</p>
                <p><strong>Phone:</strong> [Company Phone Number]</p>
            </div>
            
            <div class="footer">
                <p>This is an automated confirmation message. Please do not reply to this email.</p>
                <p>© {datetime.utcnow().year} Kingdom Foods. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return email_body