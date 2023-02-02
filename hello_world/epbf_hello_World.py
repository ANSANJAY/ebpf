#!/usr/bin/python
from bcc import BPF

prog = """
int hello(void *ctx){
    bpf_trace_printk("Hello world\\n");
    return 0;
}
"""


#attaching program to an event

b = BPF(text=prog)
clone = b.get_syscall_fnname("clone") #event clone would get_syscall_fnname
b.attach_kprobe(event=clone,fn_name="hello")
b.trace_print()

