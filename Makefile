.DEFAULT_GOAL := pkg

docs := ./docs
srcdir := ./src
pkgname := ps1api

documentation: clean
	@echo "Running docs"
	./scripts/genmedia.py check
	mm2github.py ./README.mm -w
	./scripts/gendoc.py
	./scripts/genbadges.py
	pydoctor -W \
	     --html-output=$(docs)/ \
	     --buildtime="1996-06-17 15:00:00" \
	     $(srcdir)/$(pkgname)
	./scripts/checkundocced.py

docker_test:
	./scripts/dockertest.sh

install_local:
	pip3 install .

# pkg: documentation docker_test
pkg: documentation
	@echo "Running PKG"
	python3 setup.py sdist
	twine check dist/*

upload:
	@echo "Running upload"
	twine upload --repository freeplane-tools dist/*

bump_version:
	# order is important here
	./scripts/version_bump.py
	./scripts/genchangelog.py
	git add ./CHANGELOG.md
	git add ./VERSION
	git diff HEAD
	git commit -S --amend
	bash -c "git tag v$$(cat VERSION)"

media:
	./scripts/genmedia.py create

push:
	$(eval tag = $(shell cat VERSION))
	git push -u origin HEAD
	git push -u origin v$(tag)

release: pkg upload push
	@echo "Running Release"

clean:
	rm -rfv docs/* dist/* src/*.egg-info
