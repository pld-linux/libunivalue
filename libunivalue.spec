Summary:	C++ universal value object and JSON library
Summary(pl.UTF-8):	Biblioteka C++ do obiektów uniwersalnych wartości i JSON
Name:		libunivalue
Version:	1.1.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/jgarzik/univalue/releases
Source0:	https://github.com/jgarzik/univalue/archive/v%{version}/univalue-%{version}.tar.gz
# Source0-md5:	cbead9079b14837f91513d0831e38d5d
URL:		https://github.com/jgarzik/univalue
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A universal value object, with JSON encoding (output) and decoding
(input). Built as a single dynamic RAII C++ object class, and no
templates.

%description -l pl.UTF-8
Obiekt o uniwersalnej wartości, z kodowaniem JSON (wyjście) i
dekodowaniem (wejście). Zbudowany jako pojedyncza, dynamiczna klasa
obiektów C++ RAII, bez szablonów.

%package devel
Summary:	libunivalue development package
Summary(pl.UTF-8):	Pliki dla programistów libunivalue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libunivalue development package.

%description devel -l pl.UTF-8
Pliki dla programistów używających libunivalue.

%package static
Summary:	Static libunivalue library
Summary(pl.UTF-8):	Statyczna biblioteka libunivalue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libunivalue library.

%description static -l pl.UTF-8
Statyczna biblioteka libunivalue.

%prep
%setup -q -n univalue-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build-aux/m4
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunivalue.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md TODO
%attr(755,root,root) %{_libdir}/libunivalue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunivalue.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunivalue.so
%{_includedir}/univalue.h
%{_pkgconfigdir}/libunivalue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libunivalue.a
