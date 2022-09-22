# custom-asm

a custom assembly language running in python, created by replacing the globals object in memory with ctypes to ignore undefined variables and bullying  `__annotations__`


you use the module by:
```py
import asm; __asm__(globals());
```

and then just use assembly
if you want to know how the instructions work, read __init__.py, I'm to lazy to write docs
