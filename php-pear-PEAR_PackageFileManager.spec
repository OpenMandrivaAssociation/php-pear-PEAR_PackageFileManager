%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PEAR/PackageFile.php)\\|pear(PEAR/PackageFile/Generator/v1.php)

Name:		php-pear-%{upstream_name}
Version:	1.7.0
Release:	%mkrel 2
Summary:	Takes an existing package.xml file and updates it with a new filelist and changelog
License:	New BSD License
Group:		Development/PHP
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
