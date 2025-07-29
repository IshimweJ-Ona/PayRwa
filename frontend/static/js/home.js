console.log("Home page loaded");
window.addEventListener("DOMContentLoaded", () => {
  fetch("/status")
    .then((res) => res.json())
    .then((data) => console.log("Session status:", data));
});


document.addEventListener('DOMContentLoaded', function() {
    // Initialize logo animations for both navbar and home section
    const letters = ['P', 'a', 'y', 'R', 'w', 'a'];
    const colors = ['#3498db', '#e74c3c', '#f1c40f', '#2ecc71', '#9b59b6', '#1abc9c'];

    function initializeLogo(containerId) {
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = '';
            letters.forEach((char, index) => {
                const span = document.createElement('span');
                span.textContent = char;
                span.className = 'logo-letter';
                span.style.animationDelay = `${index * 0.1}s`;
                container.appendChild(span);
            });
        }
    }

    initializeLogo('logo');
    initializeLogo('home-logo');

    const navbar = document.querySelector('.navbar');
    const menuBtn = document.querySelector('.menu-btn');
    const closeBtn = document.querySelector('.close-btn');
    const navLinks = document.querySelectorAll('.nav-links a');
    const overlay = document.querySelector('.overlay');

    function toggleMenu(show) {
        navbar.classList.toggle('active', show);
        document.body.classList.toggle('menu-open', show);
        overlay.style.display = show ? 'block' : 'none';
    }

    menuBtn?.addEventListener('click', () => toggleMenu(true));
    closeBtn?.addEventListener('click', () => toggleMenu(false));
    overlay?.addEventListener('click', () => toggleMenu(false));

    navLinks?.forEach(link => {
        link.addEventListener('click', () => {
            toggleMenu(false);
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && navbar.classList.contains('active')) {
            toggleMenu(false);
        }
    });

    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (window.innerWidth > 768 && navbar.classList.contains('active')) {
                toggleMenu(false);
            }
        }, 250);
    });
});

