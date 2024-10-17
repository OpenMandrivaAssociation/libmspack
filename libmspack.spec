%define major 0
%define libname %mklibname mspack %{major}
%define develname %mklibname mspack -d

Summary:	Library for CAB and related files compression and decompression
Name:		libmspack
Version:	0.5
Release:	0.2.alpha
Group:		System/Libraries
License:	LGPLv2
URL:		https://www.cabextract.org.uk/libmspack/
Source0:	http://www.cabextract.org.uk/libmspack/%{name}-%{version}alpha.tar.gz
Patch0:		%{name}-0.4alpha-doc.patch
BuildRequires:	doxygen

%description
The purpose of libmspack is to provide both compression and decompression of 
some loosely related file formats used by Microsoft.

%package -n	%{libname}
Summary:	Library for CAB and related files compression and decompression
Group:		System/Libraries

%description -n	%{libname}
The purpose of libmspack is to provide both compression and decompression of 
some loosely related file formats used by Microsoft.

%package -n	%{develname}
Summary:	The development libraries and header files for libmspack
Group:		Development/C
Requires:	%{libname} >= %{version}
%rename	%{name}-devel

%description -n	%{develname}
This package contains libraries, header files and documentation for developing
applications that use %{name}.

%prep

%setup -q -n %{name}-%{version}alpha
%patch0 -p1

chmod a-x mspack/mspack.h

%build
%configure2_5x \
    --disable-static \
    --disable-silent-rules
%make

%install
%makeinstall_std INSTALL='install -p'


iconv -f ISO_8859-1 -t utf8 ChangeLog --output Changelog.utf8
touch -r ChangeLog Changelog.utf8
mv Changelog.utf8 ChangeLog

pushd doc
doxygen
find html -type f | xargs touch -r %{SOURCE0}
rm -f html/installdox
popd

rm %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc README TODO COPYING.LIB ChangeLog AUTHORS
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Feb 06 2015 oden <oden> 0.5-0.1.alpha.mga5
+ Revision: 813673
- imported package libmspack

