Summary:	Battery monitor panel plugin for XFce4
Summary(pl):	Monitor zu¿ycia baterii dla panelu XFce4
Name:		xfce4-battery-plugin
Version:	0.2.0
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	ad6cbb65b356342bf1b474b612beadf4
URL:		http://www.xfce.org/
BuildRequires:	xfce4-panel-devel
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battery monitor panel plugin for XFce4.

%description -l pl
Wtyczka dla panelu XFce4 pokazuj±ca zu¿ycie baterii.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
