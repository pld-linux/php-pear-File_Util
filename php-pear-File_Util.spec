%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	File_Util
%define		subver	alpha1
%define		rel		1
Summary:	%{_pearname} - Common file and directory utility functions
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	32e7f40a0eb1a550ca61372b2c3a3dfe
URL:		http://pear.php.net/package/File_Util/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-File >= 1.4.0-0.alpha1
Requires:	php-pear-PEAR-core >= 1:1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common file and directory utility functions. Path handling, temp
dir/file, sorting of files, listDirs, isIncludable and more

In PEAR status of this package is: %{_status}.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/Util.php
