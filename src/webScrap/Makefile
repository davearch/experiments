VERSION=$(shell grep __version__ webScrap/__init__.py)

all: init

init:
	echo "Installing webScrap"
	python -m webScrap webScrap/webScrap.py

clean:
	rm -v webScrap/*.pyc
