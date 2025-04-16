import os
import sys
import time
import requests
from bs4 import BeautifulSoup
import random

PASSWORD = "grimm2025"

def banner():
    os.system("clear")
    print("""
   ██████╗ ██████╗ ██╗███╗   ███╗███╗   ███╗    ███╗   ███╗ █████╗ ██╗██╗     
  ██╔════╝██╔═══██╗██║████╗ ████║████╗ ████║    ████╗ ████║██╔══██╗██║██║     
  ██║     ██║   ██║██║██╔████╔██║██╔████╔██║    ██╔████╔██║███████║██║██║     
  ██║     ██║   ██║██║██║╚██╔╝██║██║╚██╔╝██║    ██║╚██╔╝██║██╔══██║██║██║     
  ╚██████╗╚██████╔╝██║██║ ╚═╝ ██║██║ ╚═╝ ██║    ██║ ╚═╝ ██║██║  ██║██║███████╗
   ╚═════╝ ╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                         GRIMM-MAIL | Accès sécurisé
                  Créé par Zephyr & Emperor Sukuna - 2025
    """)

def check_password():
    banner()
    mot = input("[?] Entre le mot de passe pour accéder à GRIMM-MAIL : ")
    if mot != PASSWORD:
        print("\n[!] Mot de passe incorrect. Accès refusé.")
        sys.exit()
    else:
        print("\n[+] Accès autorisé. Bienvenue GRIMM !")
        time.sleep(1)

def tempmail():
    banner()
    print("[+] Génération d’un email temporaire sécurisé...\n")
    domain_list = ["1secmail.com", "1secmail.net", "1secmail.org"]
    name = f"grimm{random.randint(1000,9999)}"
    domain = random.choice(domain_list)
    email = f"{name}@{domain}"
    print(f"[+] Adresse générée : {email}")

    while True:
        print("\n[1] Rafraîchir la boîte mail")
        print("[2] Quitter la boîte")
        choix = input("[?] Choix : ")
        if choix == "1":
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}"
                response = requests.get(url).json()
                if not response:
                    print("[!] Aucun message reçu pour le moment.")
                else:
                    print("\n--- Boîte de réception ---")
                    for msg in response:
                        print(f"De: {msg['from']} | Sujet: {msg['subject']}")
            except Exception as e:
                print(f"[!] Erreur de connexion : {e}")
        else:
            break

def numero_virtuel():
    banner()
    print("[+] Récupération des numéros gratuits sur smsreceivefree.com...\n")
    try:
        url = "https://smsreceivefree.com/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        numbers = soup.select(".number-boxes-item")

        liste = []
        for i, num in enumerate(numbers):
            country = num.select_one(".number-boxes-country").text.strip()
            number = num.select_one(".number-boxes-item-number").text.strip()
            link = "https://smsreceivefree.com" + num.find('a')['href']
            print(f"{i+1}. {number} ({country})")
            liste.append(link)

        choix_num = int(input("\n[?] Choisis un numéro (exemple 1) : ")) - 1
        service = input("[?] Pour quel service (WhatsApp, Facebook, etc) : ")
        print(f"\n[+] En attente de code pour {service}...")

        while True:
            r = requests.get(liste[choix_num])
            soup = BeautifulSoup(r.text, 'html.parser')
            messages = soup.select('table.table tbody tr')
            print("\n--- Derniers messages ---")
            if not messages:
                print("[!] Aucun message reçu.")
            else:
                for msg in messages[:5]:
                    sender = msg.select_one('td:nth-child(2)').text.strip()
                    content = msg.select_one('td:nth-child(3)').text.strip()
                    time_recv = msg.select_one('td:nth-child(4)').text.strip()
                    print(f"De: {sender} | Contenu: {content} | Reçu: {time_recv}")
            choix_refresh = input("\n[1] Rafraîchir | [2] Quitter : ")
            if choix_refresh != "1":
                break
    except Exception as e:
        print(f"[!] Une erreur est survenue : {e}")

def main_menu():
    while True:
        banner()
        print("""
[1] TempMail sécurisé (boîte de réception)
[2] Numéro virtuel gratuit (choix pays & service)
[3] Quitter
        """)
        choix = input("[?] Choisis une option : ")
        if choix == "1":
            tempmail()
        elif choix == "2":
            numero_virtuel()
        elif choix == "3":
            print("[-] Fermeture de GRIMM-MAIL.")
            break
        else:
            print("[!] Option invalide.")
        input("\nAppuie sur Entrée pour retourner au menu principal.")

if __name__ == "__main__":
    check_password()
    main_menu(
