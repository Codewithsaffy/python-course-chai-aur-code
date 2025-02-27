# python in shell 

- when we open shell with folder and import file data from another file like fn and property so it will run but when we edit in imported file so it will not run in shell because it is already imported in shell so we have to restart the shell to run the edited file in shell solution is to use reload function from importlib module

```bash
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello_chai
>>> hello_chai.p("Hello")
Hello
>>> hello_chai.hello
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    hello_chai.hello
AttributeError: module 'hello_chai' has no attribute 'hello'
>>> from importlib import reload
>>> reload(hello_chai)
<module 'hello_chai' from 'E:\\python-with-chai-aur-code\\python-in-shell\\hello_chai.py'>
>>> hello_chai.hello
'hello'
>>> 
```