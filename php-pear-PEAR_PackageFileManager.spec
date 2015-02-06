%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.7.0
Release:	7
Summary:	Takes an existing package.xml and updates it with a new filelist and changelog
License:	New BSD License
Group:		Development/PHP
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-5mdv2012.0
+ Revision: 742178
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-4
+ Revision: 679557
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-3mdv2011.0
+ Revision: 613750
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.0-2mdv2010.1
+ Revision: 467948
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 1.7.0-1mdv2009.1
+ Revision: 368334
- Update php pear PEAR_PackageFileManager to 1.7.0 version

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 360149
- New version 1.6.3

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1.a4.3mdv2009.1
+ Revision: 322577
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1.a4.2mdv2009.0
+ Revision: 237044
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1.a4.1mdv2007.0
+ Revision: 82505
- Import php-pear-PEAR_PackageFileManager

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-0.a4.2mdk
- new group (Development/PHP)

* Thu Dec 08 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-0.a4.1mdk
- 1.6.0a4

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-1mdk
- 1.5.2

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdk
- initial Mandriva package (PLD import)

