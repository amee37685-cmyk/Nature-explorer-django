# NatureScape

NatureScape is a Django website for browsing a small collection of nature-themed pages. Visitors can explore mountain, forest, beach, and sunset galleries, read an About page, and open a contact form. The project also includes Django's admin site and a SQLite database model for contact details.

## Features

- Home, About, Services, and Contact pages
- Separate gallery pages for mountains, forests, beaches, and sunsets
- Responsive page styling using Bootstrap 5.3.8 from jsDelivr
- Django admin registration for the contact model
- SQLite database configured as the default database

## Technologies

- Python
- Django (settings were generated with Django 6.1.1)
- Django templates, HTML, and CSS
- Bootstrap 5.3.8 (loaded from a CDN)
- SQLite

## Python concepts used

- Modules, imports, and package structure
- Functions and request handling
- Conditional logic based on HTTP request methods
- Django URL routing and view functions
- Django template rendering
- Django models and ORM save operations
- `pathlib.Path` for filesystem paths

## Database

The project uses SQLite, stored at `db.sqlite3` in the repository root. The `home` app defines a `contact` model with fields for name, email, password, country, gender, and message. The initial migration creates this table, and the model is registered in the Django admin.

The current contact view has a name collision between its view function and the imported model. As written, a POST submission will not successfully create a contact record until that is corrected in the application code.

## Project structure

```text
.
|-- Hello/                 # Django project settings and ASGI/WSGI entry points
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- home/                  # Site app: views, routes, model, admin, and migration
|   |-- migrations/
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- static/                # Static assets directory
|-- templates/             # HTML templates and template CSS
|-- db.sqlite3             # SQLite database
`-- manage.py              # Django management command entry point
```

## Installation

1. Install Python 3.12 or newer and make sure `python` and `pip` are available. Django 6.1 requires a compatible Python version.
2. Clone this repository and change into its project directory.
3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install Django (the repository does not include a dependency or requirements file):

   ```bash
   python -m pip install "Django>=6.1,<6.2"
   ```

## Run the project

Apply database migrations, then start Django's development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. The admin site is available at <http://127.0.0.1:8000/admin/>. Create an administrator account first with:

```bash
python manage.py createsuperuser
```

The pages use Bootstrap assets from jsDelivr, so the browser needs network access to load Bootstrap styling and scripts.

## Tests

`home/tests.py` currently contains only the default empty Django `TestCase` scaffold; no project tests are implemented. Django's test command is:

```bash
python manage.py test
```

## Reports and exports

No report generation or data export functionality is present in the source code.

## Possible future improvements

- Fix the contact view/model naming collision and add tests for valid and invalid submissions.
- Use Django's form handling and validation rather than reading raw POST fields.
- Avoid storing a password as plain text; remove it if it is not required, or use Django's secure password hashing if authentication is intended.
- Add a dependency manifest and document a supported Python/Django version range.
- Add automated tests for routes, templates, and contact persistence.
- Make gallery content configurable through models and the admin instead of hard-coded template markup.
- Add deployment settings and production security configuration.
