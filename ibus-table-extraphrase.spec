%define	version 1.2.0.20100305
%define	release %mkrel 6

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


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.2.0.20100305-5mdv2011.0
+ Revision: 669833
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0.20100305-4
+ Revision: 665495
- mass rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0.20100305-3mdv2011.0
+ Revision: 611167
- rebuild

* Sat Mar 27 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20100305-2mdv2010.1
+ Revision: 528052
- bump rel
- update to new version 1.2.0.20100305

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090415-1mdv2010.0
+ Revision: 410478
- new version 1.1.0.20090415

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090406-1mdv2010.0
+ Revision: 369441
- New version 1.1.0.20090406

* Sat Feb 21 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090219-1mdv2009.1
+ Revision: 343584
- New version 1.1.0.20090219

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.1.2.20090102-1mdv2009.1
+ Revision: 324466
- Provides devel package
- import ibus-table-extraphrase


