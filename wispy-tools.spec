%define		_ver 2006-01-R1
Summary:	Wi-SPY is a USB 2.4GHz spectrum analyzer
Summary(pl):	Wi-SPY jest analizatorem spektrum dla USB 2.4GHz
Name:		wispy-tools
Version:	2006_01_R1
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	%{name}-%{_ver}.tar.gz
# Source0-md5:	f28abc5c3e3d7f9c248288a79cb74222
Patch0:		%{name}-ncurses.patch
URL:		http://www.kismetwireless.net/wispy.shtml
BuildRequires:	autoconf
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WiSPY-Tools are a set of open-source tools for supporting the device.

%description -l pl
WiSPY-Tools s� narz�dziami open-source do wspierania urz�dzenia.

%package gtk
Summary:	Wi-SPY is a USB 2.4GHz spectrum analyzer
Summary(pl):	Wi-SPY jest analizatorem spektrum dla USB 2.4GHz
Group:		Networking/Utilities

%description gtk
WiSPY-Tools are a set of open-source tools for supporting the device.

%description gtk -l pl
WiSPY-Tools s� narz�dziami open-source do wspierania urz�dzenia.

%prep
%setup -q -n %{name}-%{_ver}
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install wispy_raw $RPM_BUILD_ROOT%{_bindir}
install wispy_curses $RPM_BUILD_ROOT%{_bindir}
install wispy_gtk $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/wispy_raw
%attr(755,root,root) %{_bindir}/wispy_curses

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wispy_gtk