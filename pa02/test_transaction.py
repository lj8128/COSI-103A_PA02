import pytest
from transactions import Transaction, to_dict_group_by, to_dict_group_by_list

#Meng-Ku Chen
@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

#Meng-Ku Chen
@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

#Meng-Ku Chen
@pytest.fixture
def med_db(empty_db):
    ''' create a small database, and tear it down later'''
    t1 = {"itemNum":1, "amount":20, "category":'food', "date":"2020-11-20", "desc":'I love food'}
    t2 = {"itemNum":2, "amount":10, "category":'food', "date":"2020-11-20", "desc":'food is good'}
    t3 = {"itemNum":3, "amount":30, "category":'drink', "date":"2010-11-20", "desc":'I love drink'}
    t4 = {"itemNum":4, "amount":40, "category":'drink', "date":"2010-11-20", "desc":'drink is good'}
    id1=empty_db.add(t1)
    id2=empty_db.add(t2)
    id3=empty_db.add(t3)
    id3 = empty_db.add(t4)
    yield empty_db

#Meng-Ku Chen
@pytest.mark.simple
def test_to_dict_group_by():
    ''' teting the to_dict_group_by function '''
    a = to_dict_group_by((2017,30), "year")
    assert a['year']== 2017
    assert a['amount']== 30
    assert len(a.keys())== 2

#Meng-Ku Chen
@pytest.mark.simple
def test_to_dict_group_by_list():
    ''' teting the to_dict_group_by_list function '''
    a = to_dict_group_by_list([(2017,30)], "year")
    assert a[0]['year']== 2017
    assert a[0]['amount']== 30
    assert len(a[0].keys()) == 2

#Meng-Ku Chen
@pytest.mark.simple
def test_summarize_transactions_by_year(med_db):
    ''' test summarize_transactions_by_year '''

    trans = med_db.summarize_transactions_by_year()
    assert len(trans) == 2
    t1 = trans[0]
    assert t1['year']== "2010"
    assert t1['amount']== 70
    t2 = trans[1]
    assert t2['year'] == "2020"
    assert t2['amount'] == 30
    assert len(t1.keys()) == 2

#Meng-Ku Chen
@pytest.mark.simple
def test_summarize_transactions_by_category(med_db):
    ''' test summarize_transactions_by_year '''

    trans = med_db.summarize_transactions_by_category()
    assert len(trans) == 2
    t1 = trans[0]
    assert t1['category']== "drink"
    assert t1['amount']== 70
    t2 = trans[1]
    assert t2['category'] == "food"
    assert t2['amount'] == 30
    assert len(t1.keys()) == 2
