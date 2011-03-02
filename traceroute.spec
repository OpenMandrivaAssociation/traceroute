Summary:	Traces the route taken by packets over an IPv4/IPv6 network
Name:		traceroute
Version:	2.0.17
Release:	%mkrel 1
Group:		Monitoring
License:	GPLv2+
URL:		http://traceroute.sourceforge.net/
Source0:	http://downloads.sourceforge.net/traceroute/%{name}-%{version}.tar.bz2
Source1:	usr.sbin.traceroute.apparmor
Patch0:		traceroute-2.0.12-format_not_a_string_literal_and_no_format_arguments.diff
Conflicts:	apparmor-profiles < 2.1-1.961.5mdv2008.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
New implementation of the traceroute utility for modern Linux systems.
Backward compatible with the traditional traceroute. Supports both IPv4 
and IPv6, additional types of trace (including TCP), allows some traces 
for unprivileged users.

The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.Traceroute is used as a network debugging
tool.If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%prep
%setup -q
%patch0 -p0

%build
%make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir}

mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.traceroute

%clean
rm -rf %{buildroot}

%posttrans
# if we have apparmor installed, reload if it's being used
if [ -x /sbin/apparmor_parser ]; then
        /sbin/service apparmor condreload
fi

%files
%defattr(-,root,root)
%doc README TODO CREDITS
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.traceroute
%attr(4755,root,bin) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
