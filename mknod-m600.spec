%define name mknod-m600
%define version 1.2
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
rm -rf %{buildroot}
install -D -m 4755 %SOURCE0 %{buildroot}/usr/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*


