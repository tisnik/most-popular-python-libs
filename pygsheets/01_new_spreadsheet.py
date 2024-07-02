import pygsheets

# inicializace klienta
client = pygsheets.authorize(service_file="clanek_secret.json")

# vytvoreni spreadsheetu
spreadsheet = client.create("Prvni tabulka")

# informace nutne pro pristup ke spreadsheetu
print("ID", spreadsheet.id)
print("Title", spreadsheet.title)
print("URL", spreadsheet.url)

# nasdileni s dalsimi uzivateli
spreadsheet.share("pavel.tisnovsky@gmail.com", role="reader", type="anyone")

# pristup k prvnimu listu
wks = spreadsheet.sheet1

# uprava bunky ve spreadsheetu
wks.update_value("A1", "Adresa")
wks.update_value("A2", "www.root.cz")

