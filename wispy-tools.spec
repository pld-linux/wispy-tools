%define		_ver 2006-01-R1
Summary:	Wi-SPY - a USB 2.4GHz spectrum analyzer
Summary(pl):	Wi-SPY - analizator widma dla USB 2.4GHz
Name:		wispy-tools
Version:	2006_01_R1
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.kismetwireless.net/code/%{name}-%{_ver}.tar.gz
# Source0-md5:	f28abc5c3e3d7f9c248288a79cb74222
Patch0:		%{name}-ncurses.patch
URL:		http://www.kismetwireless.net/wispy.shtml
BuildRequires:	autoconf
BuildRequires:	libusb-devel
Buildrequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WiSPY-Tools are a set of open-source tools for accessing the WiSPY USB
2.4GHz spectrum analyzer by Metageek LLC (http://www.metageek.net/).

This package contains:
- WiSPY Curses, a simple Curses-based grapher for data from the WiSPY
  device. Data is fetched purely in userspace via libusb.

%description -l pl
WiSPY-Tools to zbiór narzêdzi o otwartych ¼ród³ach pozwalaj±cych na
dostêp do analizatora widma 2.4GHz WiSPY USB produkcji Metageek LLC
(http://www.metageek.net/).

Ten pakiet zawiera:
- WiSPY Curses - proste narzêdzie oparte na Curses do rysowania
  wykresów danych z urz±dzenia WiSPY. DAne s± pobierane w przestrzeni
  u¿ytkownika poprzez libusb.

%package gtk
Summary:	Wi-SPY - a USB 2.4GHz spectrum analyzer
Summary(pl):	Wi-SPY - analizator widma dla USB 2.4GHz
Group:		Networking/Utilities

%description gtk
WiSPY-Tools are a set of open-source tools for accessing the WiSPY USB
2.4GHz spectrum analyzer by Metageek LLC (http://www.metageek.net/).

This package contains:
- WiSPY GTK, a GTK+ grapher for data from the WiSPY device. Data is
  fetched purely in userspace via libusb. The WiSPY GTK interface is
  modeled off the Metageek Windows application interface, although there
  are some differences.

%description gtk -l pl
WiSPY-Tools to zbiór narzêdzi o otwartych ¼ród³ach pozwalaj±cych na
dostêp do analizatora widma 2.4GHz WiSPY USB produkcji Metageek LLC
(http://www.metageek.net/).

Ten pakiet zawiera:
- WiSPY GTK - narzêdzie oparte na GTK+ do rysowania wykresów danych z
  urz±dzenia WiSPY. DAne s± pobierane w przestrzeni u¿ytkownika
  poprzez libusb. Interfejs WiSPY GTK jest zaprojektowany w oparciu o
  interfejs aplikacji Metageek pod Windows, ale jest trochê ró¿nic.

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
