version = $(shell cat VERSION)
git_hash = $(shell git rev-parse --short HEAD)

PROJECT=alfred-workflow-encode-decode

.PHONY: build package clean

all: clean build package

build:
	cp info.plist.template info.plist
	gsed -i -e "s/\$${VERSION}/${version}/" info.plist


package:
	mkdir -p dist
	zip -r dist/${PROJECT}-${version}-${git_hash}.alfredworkflow . -x \*.git\*  -x .idea\* -x token -x tags -x dist\* -x \*.swp -x info.plist.template -x \*.DS_Store\* -x \*.pyc\* -x \*snapshot\*

clean:
	rm -rf dist info.plist

test:
	python3 -m unittest *_test.py
