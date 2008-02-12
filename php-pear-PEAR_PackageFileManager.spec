%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PEAR/PackageFile.php)\\|pear(PEAR/PackageFile/Generator/v1.php)

Summary:	%{_pearname} - takes an existing package.xml file and updates it with a new filelist and changelog
Name:		php-pear-%{_pearname}
Version:	1.6.0
Release:	%mkrel 1.a4.1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}a4.tar.bz2
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package revolutionizes the maintenance of PEAR packages. With a
few parameters, the entire package.xml is automatically updated with a
listing of all files in a package.

Features include:

- manages the new package.xml 2.0 format in PEAR 1.4.0
- can detect PHP and extension dependencies using PHP_CompatInfo
- reads in an existing package.xml file, and only changes the release/changelog
- a plugin system for retrieving files in a directory. Currently two plugins
  exist, one for standard recursive directory content listing, and one that
  reads the CVS/Entries files and generates a file listing based on the
  contents of a checked out CVS repository
- incredibly flexible options for assigning install roles to files/directories
- ability to ignore any file based on a * ? wildcard-enabled string(s)
- ability to include only files that match a * ? wildcard-enabled string(s)
- ability to manage dependencies
- can output the package.xml in any directory, and read in the package.xml
  file from any directory.
- can specify a different name for the package.xml file
		 
PEAR_PackageFileManager is fully unit tested.
The new PEAR_PackageFileManager2 class is not.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install %{_pearname}-%{version}*/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}*/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}*/{examples,tests}
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


