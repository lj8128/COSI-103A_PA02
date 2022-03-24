import sqlite3

class Transaction:
    def __init__(self, filename):
        self.filename = filename
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount float, category text, date text, description text)''')
        con.commit()
        con.close()

    def add(filename,itemNum,amount,category,data,description):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute(''' INSERT INTO transcations 
                        VALUES (?,?,?,?,?)''',
                        (itemNum, amount, category, data, description))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
            
