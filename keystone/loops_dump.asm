
loops.bin:     file format binary


Disassembly of section .data:

0000000000000000 <.data>:
   0:	bb 0a 00 00 00       	mov    ebx,0xa
   5:	b8 64 00 00 00       	mov    eax,0x64
   a:	ff c8                	dec    eax
   c:	75 fc                	jne    0xa
   e:	ff cb                	dec    ebx
  10:	75 f3                	jne    0x5
