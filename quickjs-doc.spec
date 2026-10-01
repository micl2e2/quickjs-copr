%global upstream_date 2026.06.04
%global release_number 1
# Documentation only. Do not add debuginfo packages.
%global debug_package %{nil}
%global _build_id_links none

Name:           quickjs-doc
Version:        %{upstream_date}
Release:        %{release_number}%{?dist}
Summary:        QuickJS manual

License:        MIT
URL:            https://github.com/micl2e2/quickjs
Source0:        quickjs.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# NOTE for EL family chroot, add `https://dl.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/` to corresponding Copr project's Settings - Repos
BuildRequires:  pandoc

%description
HTML, PDF, Texinfo, and man-page forms of the QuickJS manual.

%prep
# The codeload archive's top directory is quickjs-<commit>.
# Unpack here without naming that directory.
%setup -q -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
# A checkout may already contain a manual. Drop it so this build
# produces doc/quickjs.html and doc/quickjs.pdf from doc/quickjs.texi.
rm -f doc/quickjs.html doc/quickjs.html.pre doc/quickjs.pdf doc/version.texi doc/quickjs.1
%make_build build_doc
# Pandoc has no Texinfo reader, and texi2any --docbook rejects this
# manual. The upstream manual is one document, so it becomes one
# section 1 page. There are no section 2–5 pages to package.
pandoc -f html -t man -s \
  -M title=quickjs \
  -M section=1 \
  -M header="QuickJS Javascript Engine" \
  -o doc/quickjs.1 doc/quickjs.html

%install
mkdir -p %{buildroot}%{_docdir}/quickjs
install -p -m 0644 doc/quickjs.html doc/quickjs.pdf doc/quickjs.texi \
    %{buildroot}%{_docdir}/quickjs/
install -D -p -m 0644 doc/quickjs.1 %{buildroot}%{_mandir}/man1/quickjs.1

%check
grep -F -q '%{upstream_date}' doc/quickjs.html
test -s doc/quickjs.pdf
grep -q '^\.TH ' doc/quickjs.1

%files
%{_docdir}/quickjs
%{_mandir}/man1/quickjs.1*

%changelog
* Thu Oct 01 2026 Packager - 2026.06.04-1
- Restart the release history
