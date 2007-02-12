Summary:	Battery monitor panel plugin for Xfce
Summary(pl.UTF-8):   Monitor zużycia baterii dla panelu Xfce
Name:		xfce4-battery-plugin
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-battery-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	c1d923bb90b79087ca7044bcc24bab5a
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-battery-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battery monitor panel plugin for Xfce.

%description -l pl.UTF-8
Wtyczka dla panelu Xfce pokazująca zużycie baterii.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-battery-plugin
%{_datadir}/xfce4/panel-plugins/battmon.desktop
%{_iconsdir}/hicolor/*/devices/*.*
