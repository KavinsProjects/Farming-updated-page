document.addEventListener('DOMContentLoaded', function() {
    // Carousel Functionality
    const slides = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.carousel-indicator span');
    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        indicators.forEach((indicator, i) => {
            indicator.classList.toggle('active', i === index);
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });

    setInterval(nextSlide, 5000); // Change slide every 5 seconds

    // Modal Functionality
    const loginModal = document.getElementById('login');
    const registerModal = document.getElementById('register');
    const closeLoginModal = document.getElementById('closeLoginModal');
    const closeRegisterModal = document.getElementById('closeRegisterModal');

    document.querySelectorAll('[href="#login"]').forEach(el => {
        el.addEventListener('click', () => loginModal.classList.remove('hidden'));
    });

    document.querySelectorAll('[href="#register"]').forEach(el => {
        el.addEventListener('click', () => registerModal.classList.remove('hidden'));
    });

    closeLoginModal.addEventListener('click', () => loginModal.classList.add('hidden'));
    closeRegisterModal.addEventListener('click', () => registerModal.classList.add('hidden'));

    // Close modal when clicking outside of the modal
    window.addEventListener('click', (e) => {
        if (e.target === loginModal) {
            loginModal.classList.add('hidden');
        }
        if (e.target === registerModal) {
            registerModal.classList.add('hidden');
        }
    });

    // Navbar hide/show on scroll
    let lastScrollTop = 0;
    const navbar = document.querySelector('.sticky-nav');
    
    window.addEventListener('scroll', () => {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > lastScrollTop) {
            navbar.classList.add('hidden');
        } else {
            navbar.classList.remove('hidden');
        }
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    });
});

