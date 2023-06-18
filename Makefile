version = $(shell cat VERSION)
git_hash = $(shell git rev-parse --short HEAD)

PROJECT=alfred-workflow-encode-decode
DEFAULT_BUMP_STAGE=beta # final|alpha|beta|candidate
DEFAULT_BUMP_SCOPE=minor # major|minor|patch
DEFAULT_BUMP_DRY_RUN=true # true|false

.PHONY: build package clean

all: clean build package

check-git-clean:
	@if ! git diff --quiet; then \
		echo "Git is dirty, please commit your changes first."; \
		exit 1; \
	fi

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



BUMP_STAGE=$(DEFAULT_BUMP_STAGE)
BUMP_SCOPE=$(DEFAULT_BUMP_SCOPE)
BUMP_DRY_RUN=$(DEFAULT_BUMP_DRY_RUN)
bump: check-git-clean
	bash ./hack/bump.sh ${BUMP_STAGE} ${BUMP_SCOPE} ${BUMP_DRY_RUN}
