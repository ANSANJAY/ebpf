Trace the UID of user creating the process

Expected output
![image](https://user-images.githubusercontent.com/97059168/216465781-9ac0c665-8b0a-4d19-b87f-456a34496582.png)

My user id as shown by : id

uid=1000(anamika) gid=1000(anamika) groups=1000(anamika),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

Expexted output of program 

              bash-265227  [003] d..31 286606.047619: bpf_trace_printk: User Id : 1000'
b''
b'            bash-264821  [000] d..31 286606.053273: bpf_trace_printk: User Id : 1000'


Expected output when run as sudo

b'           <...>-1047    [005] d..31 286593.130162: bpf_trace_printk: User Id : 0'

![image](https://user-images.githubusercontent.com/97059168/216466180-7cccc72e-7c35-4f66-bde2-2725aaf953d5.png)
