%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Ping
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Execute ping
Summary(pl):	%{_pearname} - Wywo�ywanie pinga
Name:		php-pear-%{_pearname}
Version:	2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	33af80393b7486710e7d043b2250608a
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a PHP wrapper around the ping command.

%description -l pl
Ten pakiet zawiera PHP-owy wrapper na komend� ping.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
