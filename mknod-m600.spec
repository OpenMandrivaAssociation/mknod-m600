%define name mknod-m600
%define version 1.0
%define release %mkrel 3

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


