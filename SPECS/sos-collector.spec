Summary: Capture sosreports from multiple nodes simultaneously
Name: sos-collector
Version: 1.8
Release: 2%{?dist}
Source0: http://people.redhat.com/jhunsake/sos-collector/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Url: https://github.com/sosreport/sos-collector
Requires: sos >= 3.0
Obsoletes: clustersos < 1.2.2-2
Provides: clustersos = %{version}-%{release}

Patch0: sos-collector-temp-location.patch

%if 0%{?rhel} == 7
BuildRequires: python-devel
Requires: python-futures
Requires: python-six
Requires: python-pexpect
%else
BuildRequires: python3-devel
BuildRequires: python3-six
BuildRequires: python3-pexpect
Requires: python3-six
Requires: python3-pexpect
%endif


%description
sos-collector is a utility designed to capture sosreports from multiple nodes
at once and collect them into a single archive. If the nodes are part of
a cluster, profiles can be used to configure how the sosreport command
is run on the nodes.

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?rhel} == 7
%py2_build
%else
%py3_build
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/sos-collector.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%if 0%{?rhel} == 7
%py2_install
%else
%py3_install
%endif



%check
%if 0%{?rhel} == 7
%{__python2} setup.py test
%else
%{__python3} setup.py test
%endif

%files
%{_bindir}/sos-collector
%if 0%{?rhel} == 7
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_mandir}/man1/*

%license LICENSE

%changelog
* Tue Jan 07 2020 Jake Hunsaker <jhunsake@redhat.com> - 1.8-2
- Resolves: RHBZ#1750756

* Mon Oct 14 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.8-1
- Rebase to upstream 1.8
- Resolves: RHBZ#1751633

* Fri May 24 2019 Jake Hunsaker	<jhunsake@redhat.com> - 1.7-5
- Fix local execution with pexpect
- Fix list output exception

* Thu May 02 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-3
- Backport RHHI-V cluster profile

* Thu Apr 11 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-2
- Fix 'none' cluster type enablement
- Update RHCOS image to RHEL 8 version
- Fix execution from within a container

* Mon Apr 01 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-1
- New upstream release
- Overhaul mechanism of execution of sosreport in containers
- Added RHCOS support
- Added a 'none' cluster type

* Tue Dec 11 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.6-1
- Drop paramiko dependency, use OpenSSH ControlPersist instead
- Layered cluster profiles can now accept base profile options
- Debian/Ubuntu hosts now supported

* Thu Oct 11 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-1
- New upstream release
- Resolves CVE-2018-14650

* Fri Jun 22 2018 Jake Hunsaker <jhunsake@redhat.com> 1.4-1
- New upstream release

* Thu May 24 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-3
- Fix sos-collector archive organization
- Fix cluster option validation

* Mon May 07 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-2
- Fix collection of sosreport tarballs

* Fri Apr 27 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-1
- Reset versioning to continue from clustersos

* Thu Apr 26 2018 Jake Hunsaker <jhunsake@redhat.com> 1.0-1
- Renamed project to sos-collector
- Moved github repo to sosreport org
