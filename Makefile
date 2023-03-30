.PHONY: clean all

all: index.html

clean:
	rm index.html

index.html:
	python3 generator.py
	python3 render.py once
