# we are writing two unit tests, 1. verify John's employee id  2. verify Tom's employee id

from _pytest.python import Module
from fixtures.mydb import MyDB
 
def test_johns_id():
    db=MyDB()
    conn= db.connect("server")
    cur = conn.cursor()
    id= cur.execute("select id from employee_db where name= John")
    assert id ==123


def test_toms_id():
    db=MyDB()
    conn= db.connect("server")
    cur = conn.cursor()         # we are repeating some lines of code here which is not good.
    id= cur.execute("select id from employee_db where name= Tom")
    assert id == 789

# two issues with above test code, 1. code repetition 2. creating expensiv DB connection in every test case
# Two ways to fix those issues,  1. setup and teardown methods(classis xunit style)  2. fixtures(recomended)

# from fixtures.mydb import MyDB
# conn=None
# cur=None
 
# def setup_module(module):
#     global conn
#     global cur
#     db=MyDB()
#     conn= db.connect("server")
#     cur = conn.cursor()


# def teardown_module(mmodule):
#     cur.close()
#     conn.close()
# def  test_johns_id():

#     id= cur.execute("select id from employee_db where name= John")
#     assert id == 123
# def test_toms_id():
    
#     id= cur.execute("select id from employee_db where name= Tom")
#     assert id == 789


from fixtures.mydb import MyDB
import pytest

@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db=MyDB()
    conn= db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("Closing database")




def  test_johns_id(cur):

    id= cur.execute("select id from employee_db where name= John")
    assert id == 123

def test_toms_id(cur):
    
    id= cur.execute("select id from employee_db where name= Tom")
    assert id == 789

    #fixtures leverage a concept of dependancy injection
    # fixture is better than tear down