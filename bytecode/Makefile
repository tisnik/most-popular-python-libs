listings := dis_1.list dis_2.list dis_3.list dis_4.list dis_5.list dis_6.list dis_7.list dis_8.list dis_9.list dis_A.list

all: $(listings)

clean:
	rm -f $(listings)

.PHONY: all clean

%.list: %.py
	python3 $< > $@
