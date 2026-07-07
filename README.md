# QR Code Generator — Django Web Application

A production-oriented Django application demonstrating modern web development practices, custom mixin architectures, and efficient form handling. This project showcases the ability to design scalable backend systems while maintaining clean, reusable code patterns.

---

## Overview

This Django application provides a streamlined interface for QR code generation with integrated media management, form validation, and class-based views. It demonstrates proficiency in Django conventions, object-oriented design patterns, and rapid feature implementation.

**Key Features:**
- Dynamic QR code generation from user input (text or URLs)
- Automatic image encoding with customizable parameters
- SQLite database with pre-configured media storage
- Django admin interface for content management
- Bootstrap-styled responsive forms
- Custom context management via mixin architecture

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

## Installation & Setup

### Prerequisites

Ensure your system has the following installed:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager - typically included with Python)
- **git** (for version control)
- **virtualenv** or **venv** (Python virtual environment)

### Step 1: Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/Generator_QRcode.git
cd Generator_QRcode
```

### Step 2: Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Navigate to Project Directory

```bash
cd QRcode
```

### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

**Output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The application is ready to use immediately upon cloning — no environment variables, external database connections, or additional configuration required.

---

## Project Structure

```
Generator_QRcode/
├── QRcode/                          # Django project root
│   ├── QRcode/
│   │   ├── settings.py              # Django configuration
│   │   ├── urls.py                  # URL routing
│   │   ├── wsgi.py                  # WSGI application
│   │   └── asgi.py                  # ASGI application
│   ├── generator/                   # Core application
│   │   ├── models.py                # QRCode model with generation logic
│   │   ├── views.py                 # Class-based views (CBV)
│   │   ├── forms.py                 # ModelForm for user input
│   │   ├── urls.py                  # App-level routing
│   │   └── utils.py                 # Mixin utilities
│   ├── utils/                       # Project-wide utilities
│   │   └── utils.py                 # Reusable mixin classes
│   ├── templates/                   # HTML templates
│   ├── static/                      # CSS, JavaScript, static assets
│   ├── media/                       # Generated QR code images
│   ├── db.sqlite3                   # SQLite database
│   └── manage.py                    # Django management CLI
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## Technical Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.2.8 | Web framework & ORM |
| **Python** | 3.8+ | Language runtime |
| **SQLite3** | Built-in | Relational database |
| **Pillow** | 12.1.1 | Image processing |
| **QRCode** | 8.2 | QR code generation library |

Full dependency list available in `requirements.txt`.

**External References:**
- [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/)
- [Python 3 Documentation](https://docs.python.org/3/)
- [Pillow Image Library](https://pillow.readthedocs.io/)
- [QRCode Library](https://github.com/lincolnloop/python-qrcode)

---

## Architecture & Recruitment Strategy

### Zero-Config Demo Philosophy

This repository is intentionally designed as a **zero-friction evaluation environment**. The database (`db.sqlite3`), media storage directory (`media/`), and all environment settings are included in the repository for a specific strategic reason: **to enable hiring managers and recruiters to evaluate the application in seconds**.

This represents a deliberate architectural choice, not a lack of enterprise knowledge. When a recruiter clones this repository, they can:
- ✅ Run `pip install -r requirements.txt` and `python manage.py runserver` immediately
- ✅ See the application functioning without database migrations, connection strings, or environment setup
- ✅ Verify functionality and code quality without friction
- ✅ Evaluate architectural decisions within minutes, not hours

**Rationale:** Removing setup friction is a core principle of user-centered design. In a recruitment context, setup barriers reduce the likelihood that your code will be thoroughly reviewed. This repository prioritizes the reviewer's experience.

### Accessibility Over Obfuscation

The inclusion of pre-configured database and media files reflects a priority: **accessibility to the evaluator takes precedence over conventional repository hygiene**.

In production systems, I implement industry-standard practices:
- Environment variables via `.env` files (never committed)
- Database isolation and migration management
- Cloud-based object storage (AWS S3, Azure Blob Storage)
- `.gitignore` enforcement for secrets and generated artifacts
- Infrastructure-as-code for reproducible deployments

However, for a recruitment portfolio project, those practices create **unnecessary evaluation overhead**. This repository makes a conscious trade-off: ease of evaluation > conventional repository setup patterns.

### Professional Disclaimer

**For production environments**, I adhere to security and operational best practices:

```plaintext
✓ Environment secrets managed via environment variables or secure vaults
✓ Database credentials isolated and environment-specific
✓ Media assets stored in cloud object storage (S3, GCS, etc.)
✓ .gitignore configured to exclude sensitive files
✓ Database migrations version-controlled and applied via CI/CD
✓ Static file collection and minification for performance
✓ HTTPS enforcement and security headers configured
✓ Comprehensive logging and monitoring infrastructure
```

This repository demonstrates understanding of enterprise-level architecture while making an intentional, documented choice to optimize for recruiter evaluation.

---

## Code Samples

### Model: QRCode with Business Logic

The `QRCode` model demonstrates integration of third-party libraries with Django ORM and custom save-time logic:

```python
from datetime import datetime
from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models


class QRCode(models.Model):
    content = models.CharField(max_length=255)
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.content

    def get_qr_code_image(self):
        """Return URL to generated QR image or None if not available."""
        if self.qr_image and hasattr(self.qr_image, 'url'):
            return self.qr_image.url
        return None

    def save(self, *args, **kwargs):
        """Generate QR code image on model save with configurable parameters."""
        qr_version = 1
        qr_error_correction = qrcode.ERROR_CORRECT_L
        qr_box_size = 10
        qr_border = 4

        fill_color = "black"
        back_color = "white"

        qr_image_factory = None
        qr_mask_pattern = None

        # Initialize QR code generator with parameters
        qr = qrcode.QRCode(
            version=qr_version,
            error_correction=qr_error_correction,
            box_size=qr_box_size,
            border=qr_border,
            image_factory=qr_image_factory,
            mask_pattern=qr_mask_pattern,
        )

        qr.add_data(self.content)
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        # Save to file with timestamp-based naming
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        filename = f"qr_{timestamp}.png"

        buffer = BytesIO()
        img.save(buffer, format='PNG')

        self.qr_image.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
```

**Design Highlights:**
- Encapsulation of QR generation logic within the model layer
- Timestamped file naming to prevent collisions
- In-memory image buffering for efficiency
- Graceful handling of missing images via utility method

---

### Mixin Architecture: GeneratorMixin

Demonstrates the use of mixins for cross-cutting concerns and reusable context management:

```python
class GeneratorMixin:
    """
    Mixin for views that require custom context injection.
    Provides unified method for updating context dictionaries.
    """
    def get_mixin_context(self, context: dict, **kwargs):
        """
        Safely merge additional context into the existing context dict.
        
        Args:
            context (dict): Base context dictionary from view
            **kwargs: Additional context variables to inject
            
        Returns:
            dict: Updated context dictionary
        """
        context.update(kwargs)
        return context
```

**Benefits:**
- Promotes code reuse across multiple views
- Centralizes context mutation logic
- Type hints for clarity
- Easily extended for additional views requiring similar behavior

---

### Class-Based View: QRCodeCreateView

Demonstrates modern Django patterns with form handling, messaging, and error management:

```python
from django.contrib import messages
from django.views.generic import CreateView

from .forms import QRCodeForm
from .models import QRCode
from .utils import GeneratorMixin


class QRCodeCreateView(CreateView, GeneratorMixin):
    """
    View for creating new QR codes from user input.
    Combines Django CBV with custom mixin for context management.
    """
    model = QRCode
    template_name = 'generator/generator.html'
    form_class = QRCodeForm
    context_object_name = 'qr'

    def get_form_kwargs(self):
        """
        Prepare form instantiation kwargs.
        Override point for custom form initialization.
        """
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """
        Handle successful form submission.
        Save model and display success message.
        """
        self.object = form.save()
        messages.success(
            request=self.request, 
            message='QR code successfully generated'
        )
        return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        """
        Handle form validation failure.
        Re-render form with validation errors.
        """
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        """
        Inject custom context variables using mixin pattern.
        """
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context, title='QRcode Generator')
```

**Architectural Patterns:**
- Class-based views for code organization and reusability
- Explicit method overriding for clear intent
- Django messaging framework for user feedback
- Mixin composition for separation of concerns
- Consistent error handling for both valid and invalid states

---

### Form: QRCodeForm with Bootstrap Integration

Demonstrates ModelForm usage with widget customization for responsive UI:

```python
from django import forms
from django.forms import ModelForm

from .models import QRCode


class QRCodeForm(ModelForm):
    """
    Form for QR code creation.
    Integrates Bootstrap CSS classes for responsive design.
    """
    content = forms.CharField(
        max_length=225,
        label='',  # No label; placeholder provides UX context
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL or text...',
        })
    )

    class Meta:
        model = QRCode
        fields = ['content']
```

**Features:**
- Clean separation of form logic from model definition
- Widget customization with CSS framework integration
- User-friendly placeholder text
- Single-field form aligned with business requirements

---

### Utility: FieldExtractorMixin for Development

A developer-focused utility demonstrating metaprogramming and introspection:

```python
class FieldExtractorMixin:
    """
    Development utility for rapid form inspection.
    Extracts field names from Django forms to accelerate view creation.
    """
    def get_form_fields(self, form_class):
        """
        Inspect Django form and extract field names.
        
        Args:
            form_class: A Django form class
            
        Returns:
            list: Field names if valid form class, empty list otherwise
        """
        if hasattr(form_class, 'base_fields'):
            fields_list = list(form_class.base_fields.keys())
            print("\n" + "=" * 40)
            print(f"FORM STRUCTURE: {form_class.__name__}")
            print("COPY THIS LIST OF FIELDS:")
            print(fields_list)
            print("=" * 40 + "\n")
            return fields_list
        else:
            print("Error: The passed object is not a Django form class.")
            return []
```

**Purpose:**
- Reduces repetitive manual field listing during development
- Demonstrates Python introspection and metaprogramming
- Practical tooling that improves developer experience

---

## Dependencies

```
asgiref==3.11.1      # ASGI utilities for async support
colorama==0.4.6      # Colored terminal output
Django==5.2.8        # Web framework
pillow==12.1.1       # Image processing
qrcode==8.2          # QR code generation
sqlparse==0.5.5      # SQL parsing utilities
tzdata==2025.3       # Timezone database
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Configuration

### Database Configuration (`settings.py`)

The application uses SQLite for simplicity and zero external dependencies:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',  # Pre-configured and included
    }
}
```

### Media Storage

Generated QR code images are stored locally:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Template Configuration

Templates are located in the `templates/` directory with app-specific subdirectories:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        ...
    }
]
```

---

## Usage

### Generating QR Codes

1. Navigate to the application homepage
2. Enter text or URL in the input field
3. Submit the form
4. QR code is generated and displayed immediately
5. Image is stored in the `media/qr_codes/` directory

### Django Admin Interface

Access the admin panel at `/admin/`:
- Create, read, update, and delete QR code records
- View generated images
- Manage application data

---

## Development Notes

### Adding Custom Models

To extend the application:

1. Define new model in `generator/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Register model in `generator/admin.py` for admin access

### Extending Views

Use the mixin pattern for reusable view behavior:

```python
class MyCustomView(CreateView, GeneratorMixin):
    model = MyModel
    template_name = 'template.html'
    form_class = MyForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context, custom_var='value')
```

---

## Performance Considerations

- **Image Generation:** QR codes are generated on-demand during model save, not lazily
- **Media Storage:** Local filesystem storage suitable for development; production deployments should use cloud storage
- **Database:** SQLite is performant for small-to-medium datasets; PostgreSQL recommended for production
- **Static Files:** Django development server serves static files automatically; use `collectstatic` for production

---

## Testing

The project structure supports Django's testing framework. To run tests:

```bash
python manage.py test
```

---

## Security Notes

**This application is configured for development (`DEBUG=True`). For production deployment:**

1. Set `DEBUG=False` in settings
2. Generate a new `SECRET_KEY` and manage via environment variables
3. Configure `ALLOWED_HOSTS` with your domain
4. Use HTTPS and set `SECURE_SSL_REDIRECT=True`
5. Implement CSRF protection and security headers
6. Use environment-based configuration for sensitive settings
7. Deploy behind a production WSGI server (Gunicorn, uWSGI, etc.)

---

## License

This project is provided as-is for recruitment and educational purposes.

---

## Contact & Portfolio

For inquiries or to discuss this project:
- **GitHub:** [mihaiapostol14](https://github.com/mihaiapostol14)
- **Project Repository:** [Generator_QRcode](https://github.com/mihaiapostol14/Generator_QRcode)

---

**Last Updated:** 2025  
**Django Version:** 5.2.8  
**Python Version:** 3.8+
