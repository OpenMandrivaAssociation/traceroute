Summary: Traces the route taken by packets over a TCP/IP network
Name: traceroute
Version: 1.4a12
Release: %mkrel 8
License: BSD
Group: Monitoring
URL: http://www.chiark.greenend.org.uk/ucgi/~richard/cvsweb/debfix/packages/traceroute/
Source: ftp://ftp.ee.lbl.gov/traceroute-%{version}.tar.bz2
Source1: usr.sbin.traceroute.apparmor
Patch1: traceroute-1.4a5-secfix.patch
Patch3: traceroute-1.4a5-autoroute.patch
Patch4: traceroute-1.4a5-autoroute2.patch
Patch5: traceroute-1.4a5-unaligned.patch
Patch18: traceroute-1.4a12-sparcfix.patch
# (fg) 20001003 This patch fixes traceroute segfault and root exploit
Prefix: %{_prefix}
Conflicts: apparmor-profiles < 2.1-1.961.5mdv2008.0
BuildRoot: %{_tmppath}/%{name}-root

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%prep
%setup -q
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%ifarch sparc sparc64
%patch18 -p1 -b .sparc
%endif

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DHAVE_IFF_LOOPBACK -DUSE_KERNEL_ROUTING_TABLE"
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{%{_sbindir},%{_mandir}/man8}

install traceroute ${RPM_BUILD_ROOT}/%{_sbindir}
cp traceroute.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8

mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.traceroute

%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
# if we have apparmor installed, reload if it's being used
if [ -x /sbin/apparmor_parser ]; then
        /sbin/service apparmor condreload
fi


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.traceroute
%attr(4755,root,bin)	%{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
