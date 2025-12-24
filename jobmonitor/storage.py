import csv
import os

SENT_FILE = "data/sent_links.txt"

def load_sent_links():
    if not os.path.exists(SENT_FILE):
        return set()
    with open(SENT_FILE, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

def save_sent_link(link):
    with open(SENT_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")

def save_csv(vacancies):
    with open("data/vacancies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Название", "Зарплата", "Ссылка"])
        writer.writerows(vacancies)
