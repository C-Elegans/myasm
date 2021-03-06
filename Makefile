OS := $(shell uname)
COPY=objcopy
ifeq ($(OS),Darwin)
	COPY=gobjcopy
endif

all:output.hex

output.bin:test.asm  assembler.py
	python assembler.py test.asm output.bin

output.hex:output.bin
	$(COPY) -I binary -O ihex output.bin output.hex

clean:
	rm output.bin
	rm output.hex
