Summary:	Traces the route taken by packets over an IPv4/IPv6 network
Name:		traceroute
Version:	2.1.6
Release:	1
Group:		Monitoring
License:	GPLv2+
URL:		https://traceroute.sourceforge.net/
Source0:	http://downloads.sourceforge.net/traceroute/%{name}-%{version}.tar.gz
Patch0:		06-build.patch

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
%autosetup -p1
sed -i 's!-rc!rc!g' default.rules

%build
%set_build_flags
%make_build CC=%{__cc} AR=%{__ar}

%install
%make_install prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir}

%files
%doc README TODO CREDITS
%attr(4755,root,bin) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
