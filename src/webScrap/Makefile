VERSION=$(shell grep __version__ webScrap/__init__.py)

all: init

init:
	echo "Installing webScrap"
	python -c "import webScrap"
	python webScrap/webScrap.py ${ARGS}

clean:
	rm -v webScrap/*.pyc
