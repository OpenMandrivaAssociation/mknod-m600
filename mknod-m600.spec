%define name mknod-m600
%define version 1.2
%define release %mkrel 6

Summary: Create block/character devices as normal user
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}
License: GPL
Group: File tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
Create block/character devices as normal user.

This is only useful when building images (eg: rescue, install).

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 4755 %SOURCE0 $RPM_BUILD_ROOT/usr/bin/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*




%changelog
* Thu Apr 14 2011 Antoine Ginies <aginies@mandriva.com> 1.2-3mdv2011.0
+ Revision: 652891
- svn restoration

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2011.0
+ Revision: 606649
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2010.1
+ Revision: 523322
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-3mdv2010.0
+ Revision: 426151
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 223292
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1mdv2008.1-current
+ Revision: 130034
- kill re-definition of %%buildroot on Pixel's request


* Tue Jan 23 2007 Pixel <pixel@mandriva.com> 1.0-1mdv2007.0
+ Revision: 112501
- creation
- Create mknod-m600

