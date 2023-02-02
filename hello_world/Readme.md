use bcc which makes it easy to load eBPF programs into the kernel.
running them under strace to see the system calls that are happening! For example strace -e bpf ./hello_world.py will show you the bpf() system call that loads the program into the kernel (BPF_PROG_LOAD)

You can see the accompanying slides from DockerCon.
https://speakerdeck.com/lizrice/ebpf-superpowers

