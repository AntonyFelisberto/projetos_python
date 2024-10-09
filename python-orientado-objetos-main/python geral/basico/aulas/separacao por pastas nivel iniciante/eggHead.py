A = 10
print(type(A) is int)
D = {'a':1,'b':2}
x = D.get('c',None)
print(x)
print(x is None)
######################################################################################################################################################
L = [1,2,3,4]
L1 = [2,3,4]
print(L == L1)
print(id(L))
print(id(L1))
######################################################################################################################################################
my_tuple = ('ola','ask',[1,2,3],2020)
print(my_tuple)
print(type(my_tuple))
one_item = ('string')
print(type(one_item))
one_item = ('string',)
print(type(one_item))
my_tuple_two= my_tuple + (['pizza','ford'])
print(my_tuple_two)
######################################################################################################################################################
colors = {'red','yellow','blue','green'}
rainbow = {'red','yellow','blue','green'}
AGE = 30
age = 30
rainbow_colors = {'red','yellow','blue','green'}
######################################################################################################################################################
raw_data = "asakdjaslndashjdahsd=aksjdkasljdajsd;oowpeiqpwepswiepa=sajdklajsdlkajsd;asjdkljasdjalsjdlasj=weipqiepiqwpeiqwe"
items = dict(item.split("=") for item in raw_data.split(";"))
print(items)
print(items.get("asakdjaslndashjdahsd"))
######################################################################################################################################################
x = [1,2,3]
y = [1,2,3]
x.append(4)
y.extend([4])
x.append([5,6])
y.extend([5,6])
x.append("foo")
y.extend("foo")
z=[1,2,3]
z+=[4,5]
z=z + [6,7]
print(z)
print(y)
print(x)
######################################################################################################################################################
import pytest
import commom_math
class TestCommomMath(object):
    def test_add(self):
        result = commom_math.sum(1,2)
        assert result == 3
######################################################################################################################################################
with open("input.txt") as text:
    for line in text:
        print(line)
######################################################################################################################################################
#pip install mypy
from typing import Dict,List

def add_num(a:int,b:int):
    return a+b

my_str:str
my_bool:bool
my_dict:dict[str,int] = {
    "patreon":23,
    "falcons":7
}
add_num(add_num("a",10))
######################################################################################################################################################
#pip install flask
#export FLASK_APP=name_of_the_file with flask_code.py
from flask import Flask
from flask import render_template
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/foo/')
def foo():
    return 'foo page'

@app.route('/bar/')
def bar():
    return 'bar page'

@app.route('/hello/')
@app.route('/hello/<user>')
def hello_user(user=None):
    return render_template('hello.html',name=user)

@app.route('/hello/<user>')
def hello_user(user):
    return f'hello {user}'
