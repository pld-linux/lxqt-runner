#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-runner
Name:		lxqt-runner
Version:	0.10.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	eab734eed0a904672f9367732bd5b511
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.10.0
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	lxqt-globalkeys-devel >= 0.10.0
BuildRequires:	menu-cache-devel >= 0.3.3
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-runner

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-runner
%dir %{_datadir}/lxqt/translations/lxqt-runner
