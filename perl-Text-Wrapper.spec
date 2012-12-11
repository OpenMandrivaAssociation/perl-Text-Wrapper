%define upstream_name    Text-Wrapper
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:    Simple word wrapping routine perl module
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Text::Wrapper provides simple word wrapping. It breaks long lines, but does 
not alter spacing or remove existing line breaks. If you're looking for more 
sophisticated text formatting, try the Text::Format module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 406194
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-2mdv2009.0
+ Revision: 268855
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 206827
- update to new version 1.02

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdv2008.0
+ Revision: 90082
- rebuild

* Fri May 04 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-1mdv2008.0
+ Revision: 22170
- 1.01


* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.000-3mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 1.000-2mdk
- Do not ship empty dir

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.000-1mdk
- First mandriva package

