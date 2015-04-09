all:output.hex

output.bin:test.asm
	python assembler.py test.asm output.bin

output.hex:output.bin
	objcopy -I binary -O ihex output.bin output.hex

clean:
	rm output.bin
	rm output.hex
