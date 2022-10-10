%global commit0 7b1dd734c926a23f8134b42dbfaac4d22cd6ba1d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20220301

Name:       uavs3d
Summary:    AVS3 decoder library
Version:    1.2.0
Release:    2%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
License:    BSD
URL:        https://github.com/uavs3/uavs3d

Source0:    https://github.com/uavs3/uavs3d/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:     %{name}-soname.patch

BuildRequires:  cmake3 >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  git

%description
Opensource and cross-platform AVS3 decoder that supports AVS3-P2 baseline
profile.

%package libs
Summary:    AVS3 decoder library

%description libs
Opensource and cross-platform AVS3 decoder that supports AVS3-P2 baseline
profile.

%package devel
Summary:    Header files for uavs3d library
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit0}
sed -i '/libdir/ s/"lib"/"%{_lib}"/' source/CMakeLists.txt

%build
%cmake3 \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DCMAKE_SKIP_RPATH:BOOL=YES

%cmake3_build

%install
%cmake3_install
install -p -m 755 -D %{__cmake3_builddir}/uavs3dec %{buildroot}%{_bindir}/uavs3dec

%ldconfig_scriptlets libs

%files
%{_bindir}/uavs3dec

%files libs
%license COPYING
%doc README.md
%{_libdir}/libuavs3d.so.1
%{_libdir}/libuavs3d.so.%{version}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libuavs3d.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Oct 10 2022 Simone Caronni <negativo17@gmail.com> - 1.2.0-2.20220301git7b1dd73
- Use different branches for SPEC file variations.

* Wed Mar 16 2022 Simone Caronni <negativo17@gmail.com> - 1.2.0-1.20220301git7b1dd73
- First build.
