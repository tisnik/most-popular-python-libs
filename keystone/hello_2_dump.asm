
hello_2.bin:     file format binary


Disassembly of section .data:

0000000000000000 <.data>:
   0:	48                   	rex.W
   1:	65 6c                	gs ins BYTE PTR es:[rdi],dx
   3:	6c                   	ins    BYTE PTR es:[rdi],dx
   4:	6f                   	outs   dx,DWORD PTR ds:[rsi]
   5:	20 57 6f             	and    BYTE PTR [rdi+0x6f],dl
   8:	72 6c                	jb     0x76
   a:	64 21 0a             	and    DWORD PTR fs:[rdx],ecx
   d:	00 b8 04 00 00 00    	add    BYTE PTR [rax+0x4],bh
  13:	bb 01 00 00 00       	mov    ebx,0x1
  18:	b9 00 00 00 00       	mov    ecx,0x0
  1d:	ba 0d 00 00 00       	mov    edx,0xd
  22:	cd 80                	int    0x80
  24:	b8 01 00 00 00       	mov    eax,0x1
  29:	bb 00 00 00 00       	mov    ebx,0x0
  2e:	cd 80                	int    0x80
