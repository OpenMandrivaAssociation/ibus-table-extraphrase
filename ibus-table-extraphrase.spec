%define	version 1.2.0.20100305
%define	release %mkrel 4

Name:      ibus-table-extraphrase
Summary:   Chinese extra phrases for ibus-table based IME
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:    ibus-table-extraphrase-0.1.2.20090102-noarch.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: ibus-table-devel >= 1.2.0
Provides:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch
Requires:	ibus-table >= 1.2.0

%description
This package provide Chinese extra phrases for ibus-table based IME,
such as ibus-table-zhengma, ibus-table-wubi, ibus-table-cangjie5,
ibus-table-erbi and etc.

This package will also provide a script, called ibus-table-extraphrase,
to print the path of extra_phrase.txt.bz2, which can be used when using
ibus-table-createdb to generate IME database.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/ibus-table/data/extra_phrase.txt
%{_datadir}/pkgconfig/*.pc
