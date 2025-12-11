#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Application runner agent for LXQt desktop suite
Summary(pl.UTF-8):	Agent uruchamiania aplikacji dla środowiska graficznego LXQt
Name:		lxqt-runner
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-runner/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	c0f5aca6d9eca740cf7b5c58337638bb
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	lxqt-globalkeys-devel >= 2.3.0
BuildRequires:	muparser-devel >= 2.2.5
BuildRequires:	perl-base
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application runner agent for LXQt desktop suite.

%description -l pl.UTF-8
Agent uruchamiania aplikacji dla środowiska graficznego LXQt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

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
/etc/xdg/autostart/lxqt-runner.desktop
%{_mandir}/man1/lxqt-runner.1*
# required for the lang files
%dir %{_datadir}/lxqt/translations/lxqt-runner
