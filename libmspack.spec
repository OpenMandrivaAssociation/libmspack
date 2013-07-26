Name:           libmspack
Version:        0.4
Release:        0.1.alpha%{?dist}
Summary:        Library for CAB and related files compression and decompression

Group:          System/Libraries
License:        LGPLv2
URL:            http://www.cabextract.org.uk/libmspack/
Source0:        http://www.cabextract.org.uk/libmspack/%{name}-%{version}alpha.tar.gz
Patch0:         %{name}-0.4alpha-doc.patch
BuildRequires:  doxygen


%description
The purpose of libmspack is to provide both compression and decompression of 
some loosely related file formats used by Microsoft.

%package        devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-doc < 0.2

%description    devel
The %{name}-devel package contains libraries, header files and documentation
for developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}alpha
%apply_patches

chmod a-x mspack/mspack.h


%build
%configure2_5x --disable-static --disable-silent-rules
%make


%install
%makeinstall_std
rm $RPM_BUILD_ROOT%{_libdir}/libmspack.la

iconv -f ISO_8859-1 -t utf8 ChangeLog --output Changelog.utf8
touch -r ChangeLog Changelog.utf8
mv Changelog.utf8 ChangeLog

pushd doc
doxygen
find html -type f | xargs touch -r %{SOURCE0}
rm -f html/installdox
popd


%files
%doc README TODO COPYING.LIB ChangeLog AUTHORS
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

