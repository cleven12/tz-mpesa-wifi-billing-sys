"""WSGI entry point for production servers (gunicorn, uWSGI)."""

from app import create_app, socketio

application = create_app()

if __name__ == "__main__":
    socketio.run(application)
