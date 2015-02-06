%define upstream_name KinoSearch1
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Surround highlight bits with tags
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(Lingua::Stem::Snowball)
BuildRequires:	perl(Lingua::StopWords)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel

%description
KinoSearch1 is a loose port of the Java search engine library Apache
Lucene, written in Perl and C. The archetypal application is website
search, but it can be put to many different uses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.10.0-2
+ Revision: 773607
- cleanout spec
- fix duplicated debug files
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 596735
- update to 1.01

* Sat Sep 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 575788
- pkg is arch dependent
- import perl-KinoSearch1

