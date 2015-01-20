VERSION=$(shell grep __version__ webScrap/__init__.py)

all: init

init:
	@echo Installing webScrap
	python -c "import webScrap"
	python -m compileall -l . webScrap/

clean:
	rm -v webScrap/*.pyc
	rm -v webScrap/*~

debug:
	python webScrap/webScrap.py ${ARGS}
