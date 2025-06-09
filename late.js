
tailwind.config = {
    theme: {
        extend: {
            fontFamily: {
                'inter': ['Inter', 'sans-serif'],
            },
            colors: {
                primary: '#1e40af',
                secondary: '#059669',
                accent: '#7c3aed',
                dark: '#1f2937',
            },
            animation: {
                'float': 'float 6s ease-in-out infinite',
                'slide-up': 'slideUp 0.5s ease-out',
                'fade-in': 'fadeIn 0.8s ease-out',
                'scroll': 'scroll 30s linear infinite',
                'pulse-slow': 'pulse 3s infinite',
            }
        }
    }
}

function toggleFAQ(button) {
    const allAnswers = document.querySelectorAll('.answer');
    const allButtons = document.querySelectorAll('.q1');
    const allIcons = document.querySelectorAll('.icon');

    const answer = button.nextElementSibling;
    const icon = button.querySelector('.icon');

    // Close all other open FAQs
    allAnswers.forEach(a => {
        if (a !== answer) a.classList.add('hidden');
    });

    allButtons.forEach(b => {
        if (b !== button) {
            b.classList.remove('bg-green-500', 'text-white');
        }
    });

    allIcons.forEach(i => {
        if (i !== icon) i.textContent = '+';
    });

    // Toggle current one
    const isOpen = !answer.classList.contains('hidden');
    if (isOpen) {
        answer.classList.add('hidden');
        button.classList.remove('bg-green-500', 'text-white');
        icon.textContent = '+';
    } else {
        answer.classList.remove('hidden');
        button.classList.add('bg-green-500', 'text-white');
        icon.textContent = '−';
    }
}

function toggleSearch() {
    const input = document.getElementById('searchInput');
    input.classList.toggle('hidden');
    if (!input.classList.contains('hidden')) {
      input.focus();
    }
  }

function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    document.querySelectorAll('[id$="Dropdown"]').forEach(d => {
        if (d !== dropdown) d.classList.add('hidden');
    });
    dropdown.classList.toggle('hidden');
}

// Toggle Mobile Menu
document.getElementById("mobile-menu-btn").addEventListener("click", function () {
    const menu = document.getElementById("mobile-menu");
    menu.classList.toggle("hidden");
});

// Close dropdowns when clicking outside
window.addEventListener("click", function (e) {
    if (!e.target.closest(".relative")) {
        document.querySelectorAll('[id$="Dropdown"]').forEach(d => d.classList.add('hidden'));
    }
});