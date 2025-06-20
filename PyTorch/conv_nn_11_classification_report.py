from sklearn.metrics import classification_report

y_pred = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_test = [0, 1, 2, 8, 4, 5, 6, 7, 6, 9, 0, 1, 2, 2, 4, 5, 8, 7, 8, 9]

# tisk zprávy o výsledcích klasifikace
print(classification_report(y_test, y_pred))
