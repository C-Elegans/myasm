#!/usr/bin/python
import sys
opcodes = { 'nop'   : 0,
            'add'   : 1,
            'sub'   : 2,
            'or'    : 3,
            'and'   : 4,
            'not'   : 5,
            'xor'   : 6,
            'lsl'   : 7,
            'lsr'   : 8,
            'mov'   : 9,
            'cmp'   : 10,
            'ldr'   : 11,
            'str'   : 12,
            'push'  : 13,
            'pop'   : 14,
            'jmp'   : 15,
}
registers = {
    "r0"    : 0,
    "r1"    : 1,
    "r2"    : 2,
    "r3"    : 3,
    "r4"    : 4,
    "r5"    : 5,
    "r6"    : 6,
    "r7"    : 7,
    "pc"    : 7,
}
f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'wb')
file = f.readlines()
for line in file:

    instruction = line.split()
    print instruction
    op = opcodes[instruction[0]]
    print str(op) + " ",
    if(op != opcodes["nop"]):
        rd = registers[instruction[1]]
        print str(rd) + " ",
        if(not '#' in instruction[2]):
            rs = registers[instruction[2]]
            print rs
            out = (op <<11) | (rd <<8) | (rs <<5) | 0
            print format(out,'0x')
        else:
            data = int(instruction[2][1:])
            print '#' + str(data)
            out = (op <<11) | (rd <<8) | (data <<1) | 1
            print format(out,'0x')
    else if(op == opcodes["jmp"]):
        data = int(instruction[1][1:])
        out = (op <<11) | (data<<1) | 1
    else:
        out = 0
    out_h = (out & 0xff00) >>8
    out_l = out & 0xff

    bytes_arr = [out_h,out_l]
    arr = bytearray(bytes_arr)
    o.write(arr)

o.flush()
o.close()