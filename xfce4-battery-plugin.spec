Summary:	Battery monitor panel plugin for Xfce
Summary(pl):	Monitor zu¿ycia baterii dla panelu Xfce
Name:		xfce4-battery-plugin
Version:	0.3.0
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	04e121df1ff264281e56e12a8ff5f155
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99.2
Requires:	xfce4-panel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battery monitor panel plugin for Xfce.

%description -l pl
Wtyczka dla panelu Xfce4 pokazuj±ca zu¿ycie baterii.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
