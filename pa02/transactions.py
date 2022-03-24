import sqlite3

def to_trns_dict(trns_tuple):
    ''' trns is a transaction tuple (rowid, itemNum, amount, category, date, description)'''
    trns = {'rowid':trns_tuple[0], 'itemNum':trns_tuple[1], 'amount':trns_tuple[2], 'category':trns_tuple[3], 'date':trns_tuple[4], 'description':trns_tuple[5]}
    return trns

def to_trns_dict_list(trns_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trns_dict(trn) for trn in trns_tuples]

def to_dict_group_by(transcation_tuple, type):
    transcation = {type: transcation_tuple[0],
                   'amount': transcation_tuple[1]}
    return transcation

def to_dict_group_by_list(transcation_tuples, type):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_dict_group_by(t, type) for t in transcation_tuples]


class Transaction:
    def __init__(self, filename):
        self.filename = filename
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount float, category text, date DATE, description text)''')
        con.commit()
        con.close()
    
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("SELECT rowid, * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print(to_trns_dict_list(tuples))
        return to_trns_dict_list(tuples)

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute(''' INSERT INTO transactions 
                        VALUES (?,?,?,?,?)''',
                        (item['itemNum'], item['amount'], item['category'], item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def summarize_transactions_by_year(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%Y', date), SUM(amount) as amount FROM transactions"
                    "GROUP BY strftime('%Y', date)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print(to_dict_group_by_list(tuples, "year"))
        return to_dict_group_by_list(tuples, "year")

    def summarize_transactions_by_category(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount) as amount FROM transactions"
                    "GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_dict_group_by_list(tuples, "category")
            
