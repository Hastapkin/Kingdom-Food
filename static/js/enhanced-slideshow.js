/**
 * Enhanced Slideshow for Kingdom Foods Website - Optimized
 */

class KingdomSlideshow {
    constructor(container, options = {}) {
        this.container = container;
        this.slides = Array.from(container.querySelectorAll('.slideshow-slide'));
        this.dots = Array.from(container.querySelectorAll('.dot'));
        this.prevBtn = container.querySelector('.prev-slide');
        this.nextBtn = container.querySelector('.next-slide');
        
        if (this.slides.length === 0) return;
        
        // Default options
        this.options = {
            interval: 2500,
            animationSpeed: 800,
            autoplay: true,
            pauseOnHover: true,
            ...options
        };
        
        // State
        this.currentSlide = 0;
        this.isPlaying = this.options.autoplay;
        this.slideInterval = null;
        this.isAnimating = false;
        
        // Touch support
        this.touchStartX = 0;
        this.touchEndX = 0;
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.goToSlide(0);
        
        if (this.options.autoplay) {
            this.startSlideshow();
        }
    }
    
    setupEventListeners() {
        // Navigation buttons
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => {
                this.prevSlide();
                this.restartSlideshow();
            });
        }
        
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => {
                this.nextSlide();
                this.restartSlideshow();
            });
        }
        
        // Dot navigation
        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.goToSlide(index);
                this.restartSlideshow();
            });
        });
        
        // Click on slideshow container to pause/resume
        if (this.options.pauseOnClick) {
            this.container.addEventListener('click', (e) => {
                // Prevent triggering on navigation elements
                if (!e.target.closest('.slideshow-nav') && !e.target.closest('.slideshow-dots')) {
                    if (this.isPlaying) {
                        this.stopSlideshow();
                        this.container.classList.add('paused');
                    }
                }
            });
            
            // Resume on click outside
            document.addEventListener('click', (e) => {
                if (!e.target.closest('.slideshow-container') && this.container.classList.contains('paused')) {
                    this.container.classList.remove('paused');
                    this.startSlideshow();
                }
            });
        }
        
        // Touch support
        this.setupTouchEvents();
        
        // Keyboard support
        document.addEventListener('keydown', (e) => {
            if (this.isInViewport()) {
                if (e.key === 'ArrowLeft') {
                    this.prevSlide();
                    this.restartSlideshow();
                } else if (e.key === 'ArrowRight') {
                    this.nextSlide();
                    this.restartSlideshow();
                }
            }
        });
        
        // Visibility change (pause when tab is inactive)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.stopSlideshow();
            } else if (this.options.autoplay && !this.isPlaying && !this.container.classList.contains('paused')) {
                this.startSlideshow();
            }
        });
    }
    
    setupTouchEvents() {
        // Passive event listeners for better performance
        this.container.addEventListener('touchstart', (e) => {
            this.touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });
        
        this.container.addEventListener('touchend', (e) => {
            this.touchEndX = e.changedTouches[0].screenX;
            this.handleSwipe();
        }, { passive: true });
    }
    
    handleSwipe() {
        const threshold = 50;
        const diff = this.touchEndX - this.touchStartX;
        
        if (Math.abs(diff) > threshold) {
            if (diff < 0) {
                // Swipe left -> next slide
                this.nextSlide();
            } else {
                // Swipe right -> previous slide
                this.prevSlide();
            }
            this.restartSlideshow();
        }
    }
    
    isInViewport() {
        const rect = this.container.getBoundingClientRect();
        return (
            rect.top <= window.innerHeight &&
            rect.bottom >= 0 &&
            rect.left <= window.innerWidth &&
            rect.right >= 0
        );
    }
    
    goToSlide(index) {
        if (this.isAnimating || index === this.currentSlide) return;
        
        this.isAnimating = true;
        
        // Remove active class from all slides and dots
        this.slides.forEach(slide => slide.classList.remove('active'));
        this.dots.forEach(dot => dot.classList.remove('active'));
        
        // Add active class to target slide and dot
        this.slides[index].classList.add('active');
        if (this.dots[index]) {
            this.dots[index].classList.add('active');
        }
        
        this.currentSlide = index;
        
        // Reset animation flag
        setTimeout(() => {
            this.isAnimating = false;
        }, this.options.animationSpeed);
    }
    
    nextSlide() {
        if (this.currentSlide === this.slides.length - 1) {
            goToNextPageSmooth();
        } else {
            const newIndex = (this.currentSlide + 1) % this.slides.length;
            this.goToSlide(newIndex);
        }
    }
    
    prevSlide() {
        if (this.currentSlide === 0) {
            goToPrevPageSmooth();
        } else {
            const newIndex = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
            this.goToSlide(newIndex);
        }
    }
    
    startSlideshow() {
        this.stopSlideshow();
        this.slideInterval = setInterval(() => {
            if (this.currentSlide === this.slides.length - 1) {
                goToNextPageSmooth();
            } else {
                this.nextSlide();
            }
        }, this.options.interval);
        this.isPlaying = true;
    }
    
    stopSlideshow() {
        clearInterval(this.slideInterval);
        this.isPlaying = false;
    }
    
    restartSlideshow() {
        if (this.isPlaying) {
            this.stopSlideshow();
            this.startSlideshow();
        }
    }
}

/**
 * Initialize all slideshows on page load
 */
function initSlideshows() {
    const slideshowContainers = document.querySelectorAll('.slideshow-container');
    slideshowContainers.forEach(container => {
        // Read options from data attributes
        const options = {
            autoplay: container.dataset.autoplay !== 'false',
            interval: parseInt(container.dataset.interval || 1000),
            animationSpeed: parseInt(container.dataset.speed || 800)
        };
        window.KingdomSlideshow(container, options);
    });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initSlideshows);

// --- Thứ tự các trang ---
const pageOrder = [
    { path: '/', id: 'home' },
    { path: '/pages/thailand', id: 'thailand' },
    { path: '/pages/vietnam', id: 'vietnam' },
    { path: '/pages/laos', id: 'laos' }
];
function getCurrentPageIndex() {
    const currentPath = window.location.pathname.replace(/\/$/, '');
    return pageOrder.findIndex(p => p.path === currentPath || p.path === currentPath + '/');
}
function goToNextPageSmooth() {
    const idx = getCurrentPageIndex();
    const nextIdx = (idx + 1) % pageOrder.length;
    fadeOutAndRedirect(pageOrder[nextIdx].path);
}
function goToPrevPageSmooth() {
    const idx = getCurrentPageIndex();
    const prevIdx = (idx - 1 + pageOrder.length) % pageOrder.length;
    fadeOutAndRedirect(pageOrder[prevIdx].path);
}
function fadeOutAndRedirect(url) {
    const main = document.querySelector('main#main-content') || document.body;
    main.classList.add('slideshow-fadeout');
    setTimeout(() => {
        window.location.href = url;
    }, 1000);
}
document.addEventListener('DOMContentLoaded', function() {
    const main = document.querySelector('main#main-content') || document.body;
    main.classList.add('slideshow-fadein');
});

// --- Pause/Play button logic for all slideshows ---
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.slideshow-container').forEach(function(container) {
        const pauseBtn = container.querySelector('.slideshow-pause-btn');
        if (!pauseBtn) return;
        let instance = container.__kingdomSlideshowInstance;
        let isPaused = false;
        pauseBtn.addEventListener('click', function() {
            if (!instance) return;
            if (isPaused) {
                instance.startSlideshow();
                pauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
            } else {
                instance.stopSlideshow();
                pauseBtn.innerHTML = '<i class="fas fa-play"></i>';
            }
            isPaused = !isPaused;
        });
    });
});

// Gán instance vào DOM để truy cập từ nút
(function() {
    const OldKingdomSlideshow = window.KingdomSlideshow || KingdomSlideshow;
    window.KingdomSlideshow = function(container, options) {
        const inst = new OldKingdomSlideshow(container, options);
        container.__kingdomSlideshowInstance = inst;
        if (!window.KingdomSlideshowInstances) window.KingdomSlideshowInstances = [];
        window.KingdomSlideshowInstances.push(inst);
        return inst;
    };
})();