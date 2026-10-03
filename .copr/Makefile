upstream_commit := $(shell cat upstream_commit.txt)
sources := /builddir/build/SOURCES

packages:
	dnf --quiet -y install git tree gcc

create_source_rpm:
	curl --location https://codeload.github.com/micl2e2/quickjs/tar.gz/$(upstream_commit) --output quickjs.tar.gz
	cp quickjs.tar.gz $(sources)
	cp quickjs-fc-libdir.patch $(sources)
	rpmbuild -bs $(spec)

all_source_rpm_to_workdir:
	tree ~/build
	mv ~/build/SRPMS/*.src.rpm $(outdir)

srpm: packages create_source_rpm all_source_rpm_to_workdir
	echo SRPM done

