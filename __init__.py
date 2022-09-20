from ctypes import py_object
import __main__, sys, os, atexit



class __globals__(dict):
    def __getitem__(self, key):
        __getitem__ = lambda key, self=self: {}.__class__.__getitem__(self, key)
        try:
            return __getitem__(key)
        except:
            try:
                return __getitem__("__builtins__").__getattribute__(key[1:-1])
            except:
                __getitem__("__annotations__")[key]
                return key


@type.__call__
class __proc__:
    def __init__(self):
        atexit.register((lambda: self.__del__()))
        expand = (lambda compressed: (
            expanded := [],
            {
                int    : (lambda compr: expanded.append(compr)),
                str    : (lambda compr: expanded.extend([ord(char) for char in compr][::-1])),
                tuple  : (lambda compr: [expanded.extend(expand(item)) for item in compr[::-1]]),
                list   : (lambda compr: [expanded.extend(expand(item)) for item in compr[::-1]]),
            }[type(compressed)](compressed),
            expanded
        )[-1])
        self.instmap = (lambda op, *args:
            {
                "EXIT"    : (
                    (lambda: ("EXIT    0", sys.stdout.flush(), os._exit(self.stack.pop(-1) if self.stack else 0)))
                        if len(args) == 0 else
                    (lambda: ("EXIT    1", sys.stdout.flush(), os._exit((args[0]))))
                ),
                "JMP"     : (
                    (lambda: ("JMP     0", self.__setattr__("instptr", self.labels[self.stack.pop(-1)])))
                        if len(args) == 0 else
                    (lambda: ("JMP     1", self.__setattr__("instptr", self.labelnames[args[0]] if type(args[0]) == str else self.labels[args[0]])))
                ),
                "MALLOC"  : (
                    # 1 arg, amount of bytes to free
                ),
                "FREE"    : (
                    # 2 args, address to free, amount of bytes to free
                ),
                "PTR"     : (
                    # takes 1 arg, address to create a ptr to
                ),
                "DEREF"   : (
                    # takes 2 args, ptr to deref, amount of bytes to deref
                ),
                "WRITE"   : (
                    # takes 2 args; amount of bytes to pop and address to assign them to
                ),
                "PUSH"    : (
                    (lambda: ("PUSH    0", self.stack.append(0)))
                        if len(args) == 0 else
                    (lambda: ("PUSH    *", self.stack.extend(expand(args))))
                ),
                "POP"     : (
                    (lambda: ("POP     0", self.stack.pop(-1)))
                        if len(args) == 0 else
                    (lambda: ("POP     1", {self.stack.pop(i) for i in range(-1, -args[0]-1)}))
                        if len(args) == 1 else
                    (lambda: ("POP     2", {self.stack.pop(i) for i in range(-args[0]-1, -args[1]-1)}))
                        if len(args) == 2 else
                    (lambda: ("POP     3", {self.stack.pop(i) for i in range(-args[0]-1, -args[1]-1, -args[2])}))
                        if len(args) == 3 else
                    (lambda: ("POP     *", {self.stack.pop(i) for i in args}))
                ),
                "REORD"   : (
                    (lambda: ("REORD   1", self.stack.extend([self.stack.pop(i) for i in range(-1, -args[1]-1)])))
                        if len(args) == 1 else
                    (lambda: ("REORD   2", self.stack.extend([self.stack.pop(i) for i in range(-args[0]-1, -args[1]-1)])))
                        if len(args) == 2 else
                    (lambda: ("REORD   3", self.stack.extend([self.stack.pop(i) for i in range(-args[0]-1, -args[1]-1, -args[2])])))
                        if len(args) == 3 else
                    (lambda: ("REORD   *", self.stack.extend([self.stack.pop(i) for i in args])))
                ),
                "AND"     : (
                    (lambda: ("AND     0", self.stack.append(self.stack.pop(-2) & self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("AND     1", self.stack.append(self.stack.pop(-1) & args[0])))
                        if len(args) == 1 else
                    (lambda: ("AND     2", self.stack.append(args[0] & args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "OR"      : (
                    (lambda: ("OR      0", self.stack.append(self.stack.pop(-2) | self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("OR      1", self.stack.append(self.stack.pop(-1) | args[0])))
                        if len(args) == 1 else
                    (lambda: ("OR      2", self.stack.append(args[0] | args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "XOR"     : (
                    (lambda: ("XOR     0", self.stack.append(self.stack.pop(-2) ^ self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("XOR     1", self.stack.append(self.stack.pop(-1) ^ args[0])))
                        if len(args) == 1 else
                    (lambda: ("XOR     2", self.stack.append(args[0] ^ args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "NOT"     : (
                    (lambda: ("NOT     0", self.stack.append(~self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("NOT     1", self.stack.append(~args[0])))
                        if len(args) == 1 else
                    (lambda: ...)
                ),
                "ADD"     : (
                    (lambda: ("ADD     0", self.stack.append(self.stack.pop(-2) + self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("ADD     1", self.stack.append(self.stack.pop(-1) + args[0])))
                        if len(args) == 1 else
                    (lambda: ("ADD     2", self.stack.append(args[0] + args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "SUB"     : (
                    (lambda: ("SUB     0", self.stack.append(self.stack.pop(-2) - self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("SUB     1", self.stack.append(self.stack.pop(-1) - args[0])))
                        if len(args) == 1 else
                    (lambda: ("SUB     2", self.stack.append(args[0] - args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "MUL"     : (
                    (lambda: ("MUL     0", self.stack.append(self.stack.pop(-2) * self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("MUL     1", self.stack.append(self.stack.pop(-1) * args[0])))
                        if len(args) == 1 else
                    (lambda: ("MUL     2", self.stack.append(args[0] * args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "DIV"     : (
                    (lambda: ("DIV     0", self.stack.append(self.stack.pop(-2) / self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("DIV     1", self.stack.append(self.stack.pop(-1) / args[0])))
                        if len(args) == 1 else
                    (lambda: ("DIV     2", self.stack.append(args[0] / args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "MOD"     : (
                    (lambda: ("MOD     0", self.stack.append(self.stack.pop(-2) % self.stack.pop(-1))))
                        if len(args) == 0 else
                    (lambda: ("MOD     1", self.stack.append(self.stack.pop(-1) % args[0])))
                        if len(args) == 1 else
                    (lambda: ("MOD     2", self.stack.append(args[0] % args[1])))
                        if len(args) == 2 else
                    (lambda: ...)
                ),
                "COUT"    : (
                    (lambda: ("COUT    0", sys.stdout.write(chr(self.stack.pop(-1)))))
                        if len(args) == 0 else
                    (lambda: ("COUT    1", {sys.stdout.write(chr(self.stack.pop())) for i in range(args[0])}))
                        if len(args) == 1 else
                    (lambda: ("COUT    *", {sys.stdout.write(chr(arg)) for arg in expand(args)}))
                ),
                "FLUSH"   : (
                    (lambda: ("FLUSH   0", sys.stdout.flush()))
                        if len(args) == 0 else
                    (lambda: ("FLUSH  1", sys.stdout.write("\n"*args[0]), sys.stdout.flush()))
                ),
                "CLEAR"   : (
                    (lambda: ("CLEAR   0", os.system("cls||clear")))
                        if len(args) == 0 else
                    (lambda: ...)
                ),
            }[op.upper()]
        )
        self.instrs = []
        self.stack = []
        self.heap = {}
        self.labelnames = {}
        self.labels = []
        self.instptr = 0
    def __iadd__(self, other):
        self.instrs += [self.instmap(*other)]
        return self
    def __imatmul__(self, other):
        if other not in self.labelnames:
            self.labelnames[other] = len(self.instrs)
            self.labels.append(len(self.instrs))
        return self
    def __del__(self):
        print(self.labels, self.labelnames)
        self.instrs = [self.instmap("JMP", "main")] + self.instrs
        while self.instptr < len(self.instrs):
            inst = self.instrs[self.instptr]
            try:
                inst()
                self.instptr += 1
            except Exception as err:
                print(err)
                self.__terminate__(err, inst.__code__)
        sys.stdout.flush()
        os._exit(self.stack.pop(-1) if self.stack else 0)
    def __terminate__(self, err, inst):
        sys.stdout.write("\n")
        sys.stdout.flush()
        if self.instptr == 0:
            print(f"""
No main label detected.
Create a main label by doing the following:
main;
""")
        else:
            print(f"""
error at instruction {self.instptr}:
    {err}
instruction: {inst.co_consts[1]}""")
        self.instmap("EXIT", -69)()


class __annotations__(dict):
    def __getitem__(self, key):
        try:
            __main__.__proc__ += (key,)
        except KeyError:
            pass
        return key
    def __setitem__(self, key, val):
        try:
            if key == "LABEL":
                __main__.__proc__ @= val
            elif type(val) in (tuple, list, set):
                __main__.__proc__ += (key, *val)
            else:
                __main__.__proc__ += (key, val)
        except KeyError as e:
            print(e)
            print("invalid instruction")


__main__.__proc__ = __proc__
__main__.__annotations__ = __annotations__()
__main__.__asm__ = (lambda glob: py_object.from_address(id(glob) + 8).__setattr__("value", __globals__))
