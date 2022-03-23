import sqlite3

class Transactions:
    def __init__(self, filename, itemNum, amount, category, date, description):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount float, category text, date text, description text)''')
        cur.execute('''INSERT INTO transcations 
                    VALUES (?,?,?,?,?)''',
                    (itemNum, amount, category, date, description))
        con.commit()
        con.close()