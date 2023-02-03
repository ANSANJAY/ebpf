#!/usr/bin/python
from bcc import BPF
from time import sleep


prog = """
BPF_HASH(clones);

int hello(void *ctx){
    
    u64 uid;
    u64 counter=0;
    u64 *p;


    uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    p = clones.lookup(&uid);
    if(p!=0)
    {
    counter = *p;
    }
    
    counter++;
    clones.update(&uid,&counter);
    return 0;
}
"""


#attaching program to an event

b = BPF(text=prog)
clone = b.get_syscall_fnname("clone") #event clone would get_syscall_fnname
b.attach_kprobe(event=clone,fn_name="hello")

while True:
    sleep(2)
    s = ""
    if len(b["clones"].items()):
        for k,v in b["clones"].items():
            s += "ID {}: {} \t".format(k.value,v.value)
        print(s)
    else:
        print("No entries yet")




#keep a count on how many times a each user claims a new process
#using BPF hash maps
