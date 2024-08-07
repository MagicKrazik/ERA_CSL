document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quoteForm');
    const submitButton = form.querySelector('.btn-submit');

    // Form validation
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm()) {
            submitForm();
        }
    });

    // Real-time validation
    form.querySelectorAll('input, select, textarea').forEach(element => {
        element.addEventListener('blur', function() {
            validateField(this);
        });
    });

    function validateForm() {
        let isValid = true;
        form.querySelectorAll('input, select, textarea').forEach(element => {
            if (!validateField(element)) {
                isValid = false;
            }
        });
        return isValid;
    }

    function validateField(field) {
        let isValid = true;
        const errorMessage = field.nextElementSibling;

        if (field.hasAttribute('required') && !field.value.trim()) {
            isValid = false;
            showError(field, 'Este campo es obligatorio');
        } else if (field.type === 'email' && !isValidEmail(field.value)) {
            isValid = false;
            showError(field, 'Por favor, ingrese un correo electrónico válido');
        } else if (field.id === 'telefono' && !isValidPhone(field.value)) {
            isValid = false;
            showError(field, 'Por favor, ingrese un número de teléfono válido');
        } else {
            hideError(field);
        }

        return isValid;
    }

    function showError(field, message) {
        const errorElement = field.nextElementSibling;
        if (errorElement && errorElement.classList.contains('error-message')) {
            errorElement.textContent = message;
        } else {
            const error = document.createElement('div');
            error.className = 'error-message';
            error.textContent = message;
            field.parentNode.insertBefore(error, field.nextSibling);
        }
        field.classList.add('invalid');
    }

    function hideError(field) {
        const errorElement = field.nextElementSibling;
        if (errorElement && errorElement.classList.contains('error-message')) {
            errorElement.remove();
        }
        field.classList.remove('invalid');
    }

    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function isValidPhone(phone) {
        const re = /^[+]?[(]?[0-9]{3}[)]?[-\s.]?[0-9]{3}[-\s.]?[0-9]{4,6}$/;
        return re.test(phone);
    }

    function submitForm() {
        submitButton.disabled = true;
        submitButton.textContent = 'Enviando...';

        // Simulate form submission (replace with actual AJAX call)
        setTimeout(() => {
            showThankYouMessage();
            form.reset();
            submitButton.disabled = false;
            submitButton.textContent = 'Solicitar Cotización';
        }, 2000);
    }

    function showThankYouMessage() {
        const thankYouMessage = document.createElement('div');
        thankYouMessage.className = 'thank-you-message';
        thankYouMessage.innerHTML = `
            <h2>¡Gracias por su solicitud!</h2>
            <p>Hemos recibido su petición de cotización. Nuestro equipo se pondrá en contacto con usted pronto.</p>
        `;

        form.parentNode.insertBefore(thankYouMessage, form);
        form.style.display = 'none';

        setTimeout(() => {
            thankYouMessage.remove();
            form.style.display = 'block';
        }, 5000);
    }

    // Add some interactivity to benefit items
    const benefitItems = document.querySelectorAll('.benefit-item');
    benefitItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.3s ease';
        });

        item.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});