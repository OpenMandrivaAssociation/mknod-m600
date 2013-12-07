Summary:	Create block/character devices as normal user
Name:		mknod-m600
Version:	1.2
Release:	9
License:	GPLv2
Group:		File tools
Source0:	%{name}
BuildArch:	noarch

%description
Create block/character devices as normal user.

This is only useful when building images (eg: rescue, install).

%install
install -D -m 4755 %SOURCE0 %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/*

