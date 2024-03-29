%define		_class		Net
%define		_subclass	Ping
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable
Summary:	%{_pearname} - execute ping
Summary(pl.UTF-8):	%{_pearname} - wywoływanie pinga
Name:		php-pear-%{_pearname}
Version:	2.4.5
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c6573fd61f71682c3ebceb85ab779550
URL:		http://pear.php.net/package/Net_Ping/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Net_Ping-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a PHP wrapper around the ping command.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet zawiera PHP-owy wrapper na komendę ping.

Ta klasa ma w PEAR status: %{_status}.

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
