#!/usr/bin/python
from bcc import BPF

prog = """
int hello(void *ctx){
    
    u64 uid;
    uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    bpf_trace_printk("User Id : %d\\n",uid);
    return 0;
}
"""


#attaching program to an event

b = BPF(text=prog)
clone = b.get_syscall_fnname("clone") #event clone would get_syscall_fnname
b.attach_kprobe(event=clone,fn_name="hello")
b.trace_print()

