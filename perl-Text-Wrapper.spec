%define realname   Text-Wrapper

Name:		perl-%{realname}
Version:    1.01
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Simple word wrapping routine perl module
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{realname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch: noarch

%description
Text::Wrapper provides simple word wrapping. It breaks long lines, but does 
not alter spacing or remove existing line breaks. If you're looking for more 
sophisticated text formatting, try the Text::Format module.

%prep
%setup -q -n %{realname}-%{version}

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

