#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    import os
    from django.core.management import call_command

    # Run migrations automatically on Render (Free plan workaround)
    if os.environ.get("RENDER") == "true":
        try:
            call_command("migrate", interactive=False)
        except Exception as e:
            print("Migration skipped or already applied:", e)

    main()
