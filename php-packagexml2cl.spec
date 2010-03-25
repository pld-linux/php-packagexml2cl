%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
%define		pkgname	packagexml2cl
Summary:	Program to convert PEAR package.xml to ChangeLog format
Name:		php-%{pkgname}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	xml2changelog
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program to convert PEAR package.xml to ChangeLog format.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{pkgname}
