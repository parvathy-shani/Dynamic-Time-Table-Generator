document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('.right_nav a, .top_footer .right_footer a'); // Combine selectors

    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});
