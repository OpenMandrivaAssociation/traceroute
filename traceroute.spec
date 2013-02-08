%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	Traces the route taken by packets over an IPv4/IPv6 network
Name:		traceroute
Version:	2.0.19
Release:	1
Group:		Monitoring
License:	GPLv2+
URL:		http://traceroute.sourceforge.net/
Source0:	http://downloads.sourceforge.net/traceroute/%{name}-%{version}.tar.gz
Source1:	usr.sbin.traceroute.apparmor
Patch0:		traceroute-2.0.12-format_not_a_string_literal_and_no_format_arguments.diff
Conflicts:	apparmor-profiles < 2.1-1.961.5mdv2008.0

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
%make CFLAGS="%{optflags}"

%install
%makeinstall_std prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir}

mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.traceroute

%posttrans
# if we have apparmor installed, reload if it's being used
if [ -x /sbin/apparmor_parser ]; then
        /sbin/service apparmor condreload
fi

%files
%doc README TODO CREDITS
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.traceroute
%attr(4755,root,bin) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.17-2mdv2011.0
+ Revision: 670726
- mass rebuild

* Wed Mar 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.17-1
+ Revision: 641383
- update to new version 2.0.17

* Thu Sep 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.16-1mdv2011.0
+ Revision: 579051
- update to new version 2.0.16

* Wed Jul 21 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.15-1mdv2011.0
+ Revision: 556376
- update to new version 2.0.15

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.14-1mdv2011.0
+ Revision: 553713
- update to new version 2.0.14

* Fri Nov 06 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.13-1mdv2010.1
+ Revision: 462061
- update to new version 2.0.13

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.12-3mdv2010.0
+ Revision: 427430
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.12-2mdv2009.1
+ Revision: 319098
- fix build with -Werror=format-security (P0)

* Sun Sep 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.12-1mdv2009.1
+ Revision: 289065
- update to new version 2.0.12

* Fri Jun 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.11-2mdv2009.0
+ Revision: 227621
- update URL (pointed out by Dmitry Butskoy)

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.11-1mdv2009.0
+ Revision: 209080
- fix instalation of man files
- time to merge branches traceroute with current
- drop all patches
- switch to maintained version of traceroute
- spec file clean

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4a12-9mdv2008.1
+ Revision: 179661
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.4a12-8mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Wed Sep 19 2007 Andreas Hasenack <andreas@mandriva.com> 1.4a12-8mdv2008.0
+ Revision: 91192
- ship apparmor profile and use it if apparmor is in effect

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4a12-7mdv2008.0
+ Revision: 74147
- fix build


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4a12-7mdv2007.0
+ Revision: 114746
- mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4a12-6mdk
- Rebuild

* Sun Nov 14 2004 Stefan van der Eijk <stefan@mandrake.org> 1.4a12-5mdk
- sparc fix from Aurora linux

