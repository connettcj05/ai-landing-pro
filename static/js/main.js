// Initialize Feather icons
document.addEventListener('DOMContentLoaded', function() {
    feather.replace();

    // Smooth scroll for navigation links
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

    // Auto-hide navbar on scroll
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            navbar.classList.remove('scrolled-up');
            return;
        }
        
        if (currentScroll > lastScroll && !navbar.classList.contains('scrolled-down')) {
            // Scroll down
            navbar.classList.remove('scrolled-up');
            navbar.classList.add('scrolled-down');
        } else if (currentScroll < lastScroll && navbar.classList.contains('scrolled-down')) {
            // Scroll up
            navbar.classList.remove('scrolled-down');
            navbar.classList.add('scrolled-up');
        }
        lastScroll = currentScroll;
    });

    // Automatically close alert messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show');
            setTimeout(() => alert.remove(), 150);
        }, 5000);
    });
});
