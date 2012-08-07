%define		status		alpha
%define		pearname	File_Util
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Common file and directory utility functions
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	3861d4bf90f2add2572ed1b6a602c655
URL:		http://pear.php.net/package/File_Util/
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-File >= 1.4.0-0.alpha1
Requires:	php-pear-PEAR-core >= 1:1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common file and directory utility functions. Path handling, temp
dir/file, sorting of files, listDirs, isIncludable and more

In PEAR status of this package is: %{status}.

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
