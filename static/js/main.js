/**
 * Kingdom Foods Main JavaScript - Optimized
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize core features
    setupMobileMenu();
    setupFlashMessages();
    setupFormValidation();
    setupSmoothScrolling();
    setupScrollEffects();
});

/**
 * Setup mobile menu functionality
 */
function setupMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    
    if (!mobileMenuBtn || !mainNav) return;
    
    function toggleMenu() {
        mainNav.classList.toggle('active');
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    }
    
    function closeMenu() {
        if (mainNav.classList.contains('active')) {
            mainNav.classList.remove('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        }
    }
    
    // Event listeners
    mobileMenuBtn.addEventListener('click', toggleMenu);
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.main-nav') && !event.target.closest('.mobile-menu-btn')) {
            closeMenu();
        }
    });
    
    // Close menu on window resize if too wide
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            closeMenu();
        }
    });
}

/**
 * Setup flash message handling
 */
function setupFlashMessages() {
    const closeButtons = document.querySelectorAll('.flash-messages .close-btn');
    
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.alert');
            if (alert) {
                fadeOutElement(alert);
            }
        });
    });
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alerts = document.querySelectorAll('.flash-messages .alert');
        alerts.forEach(alert => fadeOutElement(alert));
    }, 5000);
    
    function fadeOutElement(element) {
        element.style.opacity = '0';
        setTimeout(() => {
            element.style.display = 'none';
        }, 300);
    }
}

/**
 * Setup form validation
 */
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Validate on submit
        form.addEventListener('submit', function(e) {
            const isValid = validateForm(this);
            if (!isValid) {
                e.preventDefault();
                scrollToFirstError(this);
            }
        });
        
        // Remove error on input
        const fields = form.querySelectorAll('input, select, textarea');
        fields.forEach(field => {
            field.addEventListener('input', function() {
                clearFieldError(this);
            });
            
            // Also validate on blur for better UX
            field.addEventListener('blur', function() {
                validateField(this);
            });
        });
    });
    
    function validateForm(form) {
        let isValid = true;
        const requiredFields = form.querySelectorAll('[required]');
        
        // Validate required fields
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                setFieldError(field, 'This field is required');
                isValid = false;
            }
        });
        
        // Validate email fields
        const emailField = form.querySelector('input[type="email"]');
        if (emailField && emailField.value) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(emailField.value)) {
                setFieldError(emailField, 'Please enter a valid email address');
                isValid = false;
            }
        }
        
        return isValid;
    }
    
    function validateField(field) {
        if (field.hasAttribute('required') && !field.value.trim()) {
            setFieldError(field, 'This field is required');
        } else if (field.type === 'email' && field.value) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(field.value)) {
                setFieldError(field, 'Please enter a valid email address');
            }
        } else {
            clearFieldError(field);
        }
    }
    
    function setFieldError(field, message) {
        field.classList.add('error');
        
        // Remove existing error message
        const existingError = field.nextElementSibling;
        if (existingError && existingError.classList.contains('error-message')) {
            existingError.remove();
        }
        
        // Add new error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        field.parentNode.insertBefore(errorDiv, field.nextSibling);
    }
    
    function clearFieldError(field) {
        field.classList.remove('error');
        const errorMessage = field.nextElementSibling;
        if (errorMessage && errorMessage.classList.contains('error-message')) {
            errorMessage.remove();
        }
    }
    
    function scrollToFirstError(form) {
        const firstError = form.querySelector('.error');
        if (firstError) {
            const headerHeight = document.querySelector('.main-header')?.offsetHeight || 0;
            const targetPosition = firstError.offsetTop - headerHeight - 20;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            firstError.focus();
        }
    }
}

/**
 * Setup smooth scrolling for anchor links
 */
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    const headerHeight = document.querySelector('.main-header')?.offsetHeight || 0;
                    const targetPosition = target.offsetTop - headerHeight - 20;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

/**
 * Setup scroll effects (header scrolled state and back to top button)
 */
function setupScrollEffects() {
    const header = document.getElementById('main-header');
    const backToTopBtn = document.getElementById('back-to-top');
    
    function handleScroll() {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        
        // Header effect
        if (header) {
            header.classList.toggle('scrolled', scrollTop > 50);
        }
        
        // Back to top button
        if (backToTopBtn) {
            backToTopBtn.classList.toggle('visible', scrollTop > 300);
        }
    }
    
    // Throttle scroll events for better performance
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(handleScroll, 10);
    });
    
    // Back to top button click
    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
}