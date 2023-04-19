
# merged and obsoleted by xfce4-power-menager

Summary:	Battery monitor panel plugin for Xfce
Summary(pl.UTF-8):	Monitor zużycia baterii dla panelu Xfce
Name:		xfce4-battery-plugin
Version:	1.1.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-battery-plugin/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	45a64fe9b81b1374ed765a931747dcea
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-battery-plugin
BuildRequires:	glib2-devel >= 2.28.0
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battery monitor panel plugin for Xfce.

%description -l pl.UTF-8
Wtyczka dla panelu Xfce pokazująca zużycie baterii.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK,uz@Latn}

chmod 755 $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libbattery.so
%{_datadir}/xfce4/panel/plugins/battery.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
