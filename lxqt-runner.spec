#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt-runner
Name:		lxqt-runner
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	b8a400d6b7f5e02fbad68592534c9570
URL:		http://www.lxqt.org/
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.7.0
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	lxqt-globalkeys-devel >= 0.7.0
BuildRequires:	menu-cache-devel >= 0.3.3
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-runner

%prep
%setup -q -c %{name}-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-runner
%dir %{_datadir}/lxqt/lxqt-runner
%lang(ar) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ar.qm
%lang(cs) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_cs_CZ.qm
%lang(da) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_da.qm
%lang(da_DK) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_da_DK.qm
%lang(de) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_de.qm
%lang(de_DE) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_de_DE.qm
%lang(el) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_el_GR.qm
%lang(eo) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_eo.qm
%lang(es) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_es.qm
%lang(es_VE) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_es_VE.qm
%lang(eu) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_eu.qm
%lang(fi) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_fi.qm
%lang(fr) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_fr_FR.qm
%lang(hu) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_hu.qm
%lang(ia) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ia.qm
%lang(id) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_id_ID.qm
%lang(it) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_it_IT.qm
%lang(ja) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ja.qm
%lang(ko) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ko.qm
%lang(lt) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_lt.qm
%lang(nl) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_nl.qm
%lang(pl) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_pl_PL.qm
%lang(pt) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_pt.qm
%lang(pt_BR) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_pt_BR.qm
%lang(ro) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ro_RO.qm
%lang(ru) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ru.qm
%lang(ru_RU) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_ru_RU.qm
%lang(sk) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_sk_SK.qm
%lang(sl) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_sl.qm
%lang(sr) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_sr_RS.qm
%lang(th) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_th_TH.qm
%lang(tr) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_tr.qm
%lang(uk) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_uk.qm
%lang(zh_CN) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt/lxqt-runner/lxqt-runner_zh_TW.qm
