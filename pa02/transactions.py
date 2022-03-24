"""
Transacation module
"""
import sqlite3

#Alex Romer
def to_trns_dict(trns_tuple):
    ''' trns is a transaction tuple (rowid, itemNum, amount, category, date, description)'''
    trns = {'rowid':trns_tuple[0], 'itemNum':trns_tuple[1], 'amount':trns_tuple[2],
            'category':trns_tuple[3], 'date':trns_tuple[4], 'description':trns_tuple[5]}
    return trns

#Alex Romer
def to_trns_dict_list(trns_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trns_dict(trn) for trn in trns_tuples]

#Meng-Ku Chen
def to_dict_group_by(transcation_tuple, t):
    ''' convert a list of category tuples into a list of dictionaries'''
    transcation = {t: transcation_tuple[0],
                   'amount': transcation_tuple[1]}
    return transcation
#Meng-Ku Chen
def to_dict_group_by_list(transcation_tuples, type):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_dict_group_by(t, type) for t in transcation_tuples]


class Transaction:
    #Alex Romer
    ''' transaction class definition'''
    def __init__(self, filename):
        self.filename = filename
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount float, category text, date DATE, description text)''')
        con.commit()
        con.close()

    #Alex Romer
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("SELECT rowid, * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trns_dict_list(tuples)

    #Alex Romer
    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute(''' INSERT INTO transactions
                        VALUES (?,?,?,?,?)''',
                        (item['itemNum'], item['amount'], item['category'],
                         item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # Meng-Ku Chen
    def summarize_transactions_by_year(self):
        ''' summarize transactins by year'''
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%Y', date), SUM(amount) as amount FROM transactions"
                    "GROUP BY strftime('%Y', date)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print(to_dict_group_by_list(tuples, "year"))
        return to_dict_group_by_list(tuples, "year")

    # Meng-Ku Chen
    def summarize_transactions_by_category(self):
        ''' summarize transactins by category'''
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount) as amount FROM transactions"
                    "GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_dict_group_by_list(tuples, "category")

    def delete(self, numOfItem):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        delete_stmt = "DELETE FROM transactions WHERE itemNum = ?"
        cur.execute(delete_stmt, (numOfItem,))
        con.commit()
        con.close()

    def summarize_transactions_by_date(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount) as amount FROM transactions"
                    "GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print(to_dict_group_by_list(tuples, "date"))
        return to_dict_group_by_list(tuples, "date")

    def summarize_transactions_by_month(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%m', date), SUM(amount) as amount FROM transactions"
                    "GROUP BY strftime('%m', date)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print(to_dict_group_by_list(tuples, "month"))
        return to_dict_group_by_list(tuples, "month")


    

