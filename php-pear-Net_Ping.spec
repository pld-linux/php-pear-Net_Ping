%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Ping
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable

Summary:	%{_pearname} - execute ping
Summary(pl):	%{_pearname} - wywo³ywanie pinga
Name:		php-pear-%{_pearname}
Version:	2.4
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0c6aecc5f3139e49b2c49ecd2e222c37
URL:		http://pear.php.net/package/Net_Ping/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a PHP wrapper around the ping command.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet zawiera PHP-owy wrapper na komendê ping.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
