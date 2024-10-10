#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pygsheets

# inicializace klienta
client = pygsheets.authorize(service_file="clanek_secret.json")

# vytvoreni spreadsheetu
spreadsheet = client.create("Druha tabulka")

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

# uprava bunky ve spreadsheetu
wks.update_value("A1", "Adresa")
wks.update_value("A2", "www.root.cz")

