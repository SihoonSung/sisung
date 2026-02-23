document.addEventListener('DOMContentLoaded', function () {

    // ═══════════════════════════════════════
    // PARTICLE ANIMATION
    // ═══════════════════════════════════════
    const canvas = document.getElementById('particle-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let particles = [];
        let animId;

        function resizeCanvas() {
            const hero = canvas.parentElement;
            canvas.width = hero.offsetWidth;
            canvas.height = hero.offsetHeight;
        }

        class Particle {
            constructor() {
                this.reset();
            }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2 + 0.5;
                this.speedX = (Math.random() - 0.5) * 0.4;
                this.speedY = (Math.random() - 0.5) * 0.4;
                this.opacity = Math.random() * 0.5 + 0.1;
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
                if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(212, 168, 75, ${this.opacity})`;
                ctx.fill();
            }
        }

        function initParticles() {
            particles = [];
            const count = Math.min(80, Math.floor((canvas.width * canvas.height) / 12000));
            for (let i = 0; i < count; i++) {
                particles.push(new Particle());
            }
        }

        function connectParticles() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 150) {
                        const opacity = (1 - dist / 150) * 0.15;
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(212, 168, 75, ${opacity})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
        }

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            connectParticles();
            animId = requestAnimationFrame(animateParticles);
        }

        resizeCanvas();
        initParticles();
        animateParticles();

        window.addEventListener('resize', () => {
            resizeCanvas();
            initParticles();
        });
    }

    // ═══════════════════════════════════════
    // TYPING EFFECT
    // ═══════════════════════════════════════
    const subtitleEl = document.getElementById('typed-subtitle');
    if (subtitleEl) {
        const phrases = [
            'CS Senior at Stony Brook University',
            'Aspiring Product Manager',
            'Security-Focused Developer',
            'CEO of CO;Ders Us'
        ];
        let phraseIdx = 0;
        let charIdx = 0;
        let isDeleting = false;
        let speed = 80;

        function typeEffect() {
            const current = phrases[phraseIdx];
            if (isDeleting) {
                subtitleEl.textContent = current.substring(0, charIdx - 1);
                charIdx--;
                speed = 40;
            } else {
                subtitleEl.textContent = current.substring(0, charIdx + 1);
                charIdx++;
                speed = 80;
            }

            if (!isDeleting && charIdx === current.length) {
                speed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIdx === 0) {
                isDeleting = false;
                phraseIdx = (phraseIdx + 1) % phrases.length;
                speed = 400;
            }

            setTimeout(typeEffect, speed);
        }

        setTimeout(typeEffect, 600);
    }

    // ═══════════════════════════════════════
    // NAVBAR SCROLL EFFECTS
    // ═══════════════════════════════════════
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-menu a:not(.nav-resume-btn)');

    function updateNavbar() {
        const scrollY = window.pageYOffset;

        // Scrolled state
        if (scrollY > 80) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Active section highlighting
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + sectionId) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    // ═══════════════════════════════════════
    // SCROLL PROGRESS BAR
    // ═══════════════════════════════════════
    const progressBar = document.getElementById('scrollProgress');

    function updateProgress() {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        if (progressBar) {
            progressBar.style.width = scrolled + '%';
        }
    }

    // ═══════════════════════════════════════
    // SCROLL REVEAL
    // ═══════════════════════════════════════
    const revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach((entry, idx) => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay);
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach((el, index) => {
        // Staggered delay for sibling items
        const parent = el.parentElement;
        const siblings = parent.querySelectorAll('.reveal');
        const siblingIndex = Array.from(siblings).indexOf(el);
        el.dataset.delay = siblingIndex * 100;
        revealObserver.observe(el);
    });

    // ═══════════════════════════════════════
    // SMOOTH SCROLL FOR NAV LINKS
    // ═══════════════════════════════════════
    const allNavLinks = document.querySelectorAll('.nav-menu a[href^="#"], .hero-buttons a[href^="#"]');

    allNavLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    const navHeight = navbar.offsetHeight;
                    const targetPosition = targetElement.offsetTop - navHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ═══════════════════════════════════════
    // COMBINED SCROLL LISTENER
    // ═══════════════════════════════════════
    let ticking = false;
    window.addEventListener('scroll', function () {
        if (!ticking) {
            requestAnimationFrame(() => {
                updateNavbar();
                updateProgress();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Initial calls
    updateNavbar();
    updateProgress();
});
