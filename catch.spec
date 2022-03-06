%define debug_package %nil

%define oname Catch
%define name %(echo %oname | tr [:upper:] [:lower:])

%define major 2
%define devname %mklibname %{name} -d
%define libname %mklibname %{name} %major

Summary:	A modern, C++-native, header-only, framework for unit-tests, TDD and BDD
Name:		%{name}
Version:	%{major}.13.8
Release:	1
Group:		System/Libraries
License:	Boost Software License
URL:		https://github.com/catchorg/%{oname}%{major}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:	cmake
BuildRequires:	ninja

%description
Catch stands for C++ Automated Test Cases in Headers and is a multi-paradigm
automated test framework for C++ and Objective-C (and, maybe, C). It is
implemented entirely in a set of header files, but is packaged up as a
single header for extra convenience.

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and docs for the %{oname} library
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Catch stands for C++ Automated Test Cases in Headers and is a multi-paradigm
automated test framework for C++ and Objective-C (and, maybe, C). It is
implemented entirely in a set of header files, but is packaged up as a
single header for extra convenience.

%files -n %{devname}
%license LICENSE.txt
%doc README.md
%doc docs
%{_includedir}/%{name}%{major}/
%{_datadir}/%{oname}%{major}/
%{_datadir}/pkgconfig/%{name}%{major}.pc
%{_libdir}/cmake/%{oname}%{major}/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{oname}%{major}-%{version}

%build
%cmake \
	-DCATCH_BUILD_EXAMPLES:BOOL=OFF \
	-DCATCH_BUILD_EXTRA_TESTS:BOOL=OFF \
	-DCATCH_BUILD_STATIC_LIBRARY:BOOL=OFF \
	-DCATCH_BUILD_TESTING:BOOL=ON \
	-DCATCH_ENABLE_COVERAGE:BOOL=OFF \
	-DCATCH_ENABLE_WERROR:BOOL=ON \
	-DCATCH_INSTALL_DOCS:BOOL=ON \
	-DCATCH_INSTALL_HELPERS:BOOL=ON \
	-DCATCH_USE_VALGRIND:BOOL=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# remove docs
rm -rf %{buildroot}/%{_docdir}

