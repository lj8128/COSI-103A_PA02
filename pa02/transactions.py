import sqlite3

def to_trns_dict(trns_tuple):
    ''' trns is a transaction tuple (rowid, itemNum, amount, category, date, description)'''
    trns = {'rowid':trns_tuple[0], 'itemNum':trns_tuple[1], 'amount':trns_tuple[2], 'category':trns_tuple[3], 'date':trns_tuple[4], 'description':trns_tuple[5]}
    return trns

def to_trns_dict_list(trns_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trns_dict(trn) for trn in trns_tuples]

class Transaction:
    def __init__(self, filename):
        self.filename = filename
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount float, category text, date text, description text)''')
        con.commit()
        con.close()
    
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trns_dict_list(tuples)

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute(''' INSERT INTO transcations 
                        VALUES (?,?,?,?,?)''',
                        (item['itemNum'], item['amount'], category['category'], data['data'], description['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
            
