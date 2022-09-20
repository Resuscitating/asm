import asm; __asm__(globals())

LABEL: pusher;
PUSH: "llo world";
PUSH: 69;
PUSH: "h"
JMP: printer;

LABEL: main;
JMP: pusher;

LABEL: printer;
COUT: 11;
JMP: exiter;


LABEL: exiter;
EXIT: 0;
