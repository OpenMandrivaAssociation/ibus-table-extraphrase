Summary:	Chinese extra phrases for ibus-table based IME
Name:		ibus-table-extraphrase
Version:	1.3.9.20110826
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Patch0:		ibus-table-extraphrase-0.1.2.20090102-noarch.patch
BuildRequires:	python-devel
BuildRequires:	ibus-table-devel
Requires:	ibus-table
BuildArch:	noarch

%description
This package provide Chinese extra phrases for ibus-table based IME,
such as ibus-table-zhengma, ibus-table-wubi, ibus-table-cangjie5,
ibus-table-erbi and etc.

This package will also provide a script, called ibus-table-extraphrase,
to print the path of extra_phrase.txt.bz2, which can be used when using
ibus-table-createdb to generate IME database.

%files
%{_datadir}/ibus-table/data/extra_phrase.txt
%{_datadir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

