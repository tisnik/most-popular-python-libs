
hello.bin:     file format binary


Disassembly of section .data:

0000000000000000 <.data>:
   0:	b8 04 00 00 00       	mov    eax,0x4
   5:	bb 01 00 00 00       	mov    ebx,0x1
   a:	b9 22 00 00 00       	mov    ecx,0x22
   f:	ba 0d 00 00 00       	mov    edx,0xd
  14:	cd 80                	int    0x80
  16:	b8 01 00 00 00       	mov    eax,0x1
  1b:	bb 00 00 00 00       	mov    ebx,0x0
  20:	cd 80                	int    0x80
  22:	48                   	rex.W
  23:	65 6c                	gs ins BYTE PTR es:[rdi],dx
  25:	6c                   	ins    BYTE PTR es:[rdi],dx
  26:	6f                   	outs   dx,DWORD PTR ds:[rsi]
  27:	20 57 6f             	and    BYTE PTR [rdi+0x6f],dl
  2a:	72 6c                	jb     0x98
  2c:	64 21 0a             	and    DWORD PTR fs:[rdx],ecx
	...
