import pygsheets

# inicializace klienta
client = pygsheets.authorize(service_file="clanek_secret.json")

# vytvoreni spreadsheetu
spreadsheet = client.create("Treti tabulka")

# informace nutne pro pristup ke spreadsheetu
print("ID", spreadsheet.id)
print("Title", spreadsheet.title)
print("URL", spreadsheet.url)

# nasdileni s dalsimi uzivateli
spreadsheet.share("pavel.tisnovsky@gmail.com", role="writer", type="anyone")

# vytvoreni dalsich listu
spreadsheet.add_worksheet(title="Druhy")
spreadsheet.add_worksheet(title="Treti")

# pristup k prvnimu listu
wks = spreadsheet.sheet1

# zmena titulku prvniho listu
wks.title = "Prvni"

# uprava bunky ve spreadsheetu
wks.update_value("A1", "Adresa")
wks.update_value("A2", "www.root.cz")

