%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Ping
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Execute ping
Summary(pl):	%{_class}_%{_subclass} - Wywo³ywanie pinga
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
Provides:       pear(%{_class}_%{_subclass})
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a PHP wrapper around the ping command.

%description -l pl
Ten pakiet zawiera PHP-owy wrapper na komendê ping.

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
