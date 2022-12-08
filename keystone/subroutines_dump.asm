
subroutines.bin:     file format binary


Disassembly of section .data:

0000000000000000 <.data>:
   0:	48                   	rex.W
   1:	65 6c                	gs ins BYTE PTR es:[rdi],dx
   3:	6c                   	ins    BYTE PTR es:[rdi],dx
   4:	6f                   	outs   dx,DWORD PTR ds:[rsi]
   5:	20 57 6f             	and    BYTE PTR [rdi+0x6f],dl
   8:	72 6c                	jb     0x76
   a:	64 0a 00             	or     al,BYTE PTR fs:[rax]
   d:	41 73 73             	rex.B jae 0x83
  10:	65 6d                	gs ins DWORD PTR es:[rdi],dx
  12:	62                   	(bad)  
  13:	6c                   	ins    BYTE PTR es:[rdi],dx
  14:	65 72 20             	gs jb  0x37
  17:	6a 65                	push   0x65
  19:	20 66 61             	and    BYTE PTR [rsi+0x61],ah
  1c:	6a 6e                	push   0x6e
  1e:	0a 00                	or     al,BYTE PTR [rax]
  20:	e8 0a 00 00 00       	call   0x2f
  25:	e8 15 00 00 00       	call   0x3f
  2a:	e8 2d 00 00 00       	call   0x5c
  2f:	b9 00 00 00 00       	mov    ecx,0x0
  34:	ba 0d 00 00 00       	mov    edx,0xd
  39:	e8 11 00 00 00       	call   0x4f
  3e:	c3                   	ret    
  3f:	b9 0d 00 00 00       	mov    ecx,0xd
  44:	ba 12 00 00 00       	mov    edx,0x12
  49:	e8 01 00 00 00       	call   0x4f
  4e:	c3                   	ret    
  4f:	b8 04 00 00 00       	mov    eax,0x4
  54:	bb 01 00 00 00       	mov    ebx,0x1
  59:	cd 80                	int    0x80
  5b:	c3                   	ret    
  5c:	b8 01 00 00 00       	mov    eax,0x1
  61:	bb 00 00 00 00       	mov    ebx,0x0
  66:	cd 80                	int    0x80
