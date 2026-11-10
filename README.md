# Network & Security Tools

Collection d'outils Python pour le diagnostic réseau et la sécurité Web.

## Outils disponibles

### 1. check_port.py
Vérifie si un port TCP est libre ou occupé sur la machine locale (127.0.0.1).

Usage :
python3 check_port.py <port>

Exemple :
python3 check_port.py 5000

---

### 2. idor_scanner.py
Scanne une plage d'IDs pour détecter des failles d'accès IDOR en comparant la taille des réponses HTTP.

Usage :
python3 idor_scanner.py <url> <cookie>

Exemple :
python3 idor_scanner.py http://127.0.0.1:5001 abc123
