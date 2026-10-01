# Metapackage. Installing it pulls in the binary, devel, and doc packages.
%global upstream_date 2026.06.04
%global release_number 1
%global debug_package %{nil}

Name:           quickjs-full
Version:        %{upstream_date}
Release:        %{release_number}%{?dist}
Summary:        QuickJS interpreter, libraries, and manual

License:        MIT
URL:            https://github.com/micl2e2/quickjs
BuildArch:      noarch

Requires:       quickjs-bin >= %{version}
Requires:       quickjs-devel >= %{version}
Requires:       quickjs-doc >= %{version}

%description
Metapackage for QuickJS. It contains no files of its own. Installing
it installs quickjs-bin, quickjs-devel, and quickjs-doc.

%files

%changelog
* Thu Oct 01 2026 Packager - 2026.06.04-1
- Restart the release history
