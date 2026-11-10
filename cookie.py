import requests
import sys


if len(sys.argv) < 3:
    print("Usage: python script.py <url> <cookie>")
    sys.exit(1)

    
arg1 = sys.argv[1]
arg2 = sys.argv[2]

s = requests.Session()

url = arg1

cookie = arg2

s.cookies.set("session", cookie)

for i in range(0,11):
    r = s.get(f"{url}/my-account?id={i}", timeout=5)
    print(f"[ID: {i}] : Status : {r.status_code} | Taille : {len(r.text)}")
