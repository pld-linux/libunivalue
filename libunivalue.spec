Summary:	C++ universal value object and JSON library
Name:		libunivalue
Version:	1.0.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/jgarzik/univalue/archive/v%{version}.tar.gz
# Source0-md5:	60bb4f4dc06fba544bf2e0b0aad815b3
URL:		https://github.com/jgarzik/univalue
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A universal value object, with JSON encoding (output) and decoding
(input). . Built as a single dynamic RAII C++ object class, and no
templates.

%package devel
Summary:	libunivalue development package
Summary(pl.UTF-8):	Pliki dla programistów libunivalue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libunivalue development package.

%description devel -l pl.UTF-8
Pliki dla programistów używających libunivalue.

%prep
%setup -q -n univalue-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md TODO
%attr(755,root,root) %ghost %{_libdir}/libunivalue.so.0
%attr(755,root,root) %{_libdir}/libunivalue.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunivalue.so
%{_includedir}/univalue.h
%{_pkgconfigdir}/libunivalue.pc
