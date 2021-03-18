#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parse-ExuberantCTags
Version  : 1.02
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Parse-ExuberantCTags-1.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Parse-ExuberantCTags-1.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libparse-exuberantctags-perl/libparse-exuberantctags-perl_1.02-1.debian.tar.xz
Summary  : Efficiently parse exuberant ctags files
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Parse-ExuberantCTags-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Parse::ExuberantCTags - Efficiently parse exuberant ctags files
SYNOPSIS
use Parse::ExuberantCTags;
my $parser = Parse::ExuberantCTags->new( 'tags_filename' );

# find a given tag that starts with 'foo' and do not ignore case
my $tag = $parser->findTag("foo", ignore_case => 0, partial => 1);
if (defined $tag) {
print $tag->{name}, "\n";
}
$tag = $parser->findNextTag();
# ...

# iterator interface (use findTag instead, it does a binary search)
$tag = $parser->firstTag;
while (defined($tag = $parser->nextTag)) {
# use the tag structure
}

%package dev
Summary: dev components for the perl-Parse-ExuberantCTags package.
Group: Development
Provides: perl-Parse-ExuberantCTags-devel = %{version}-%{release}
Requires: perl-Parse-ExuberantCTags = %{version}-%{release}

%description dev
dev components for the perl-Parse-ExuberantCTags package.


%package perl
Summary: perl components for the perl-Parse-ExuberantCTags package.
Group: Default
Requires: perl-Parse-ExuberantCTags = %{version}-%{release}

%description perl
perl components for the perl-Parse-ExuberantCTags package.


%prep
%setup -q -n Parse-ExuberantCTags-1.02
cd %{_builddir}
tar xf %{_sourcedir}/libparse-exuberantctags-perl_1.02-1.debian.tar.xz
cd %{_builddir}/Parse-ExuberantCTags-1.02
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Parse-ExuberantCTags-1.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parse::ExuberantCTags.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/Parse/ExuberantCTags.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Parse/ExuberantCTags/ExuberantCTags.so
