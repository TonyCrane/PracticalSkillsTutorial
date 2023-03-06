LECNO = 0

.PHONY: live build all clean

live:
	@echo "Previewing lec$(LECNO) slides..."
	-@reveal-md lec$(LECNO).md -w --scripts https://cdn.tonycrane.cc/heti/heti.js,heti_worker.js || true

build:
	@echo "Building lec$(LECNO) slides..."
	@reveal-md lec$(LECNO).md --scripts https://cdn.tonycrane.cc/heti/heti.js,heti_worker.js --static ../../site/lec$(LECNO) --assets-dir assets

all:
	@echo "Building all slides..."
	@for i in `seq 0 6`; do \
		make LECNO=$$i build; \
	done

clean:
	@echo "Cleaning up..."
	rm -rf ../../site/lec*
