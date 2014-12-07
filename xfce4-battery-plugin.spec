Summary:	Battery monitor panel plugin for Xfce
Summary(pl.UTF-8):	Monitor zużycia baterii dla panelu Xfce
Name:		xfce4-battery-plugin
Version:	1.0.5
Release:	5
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-battery-plugin/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	ca2d394e411a20442a519efa0d14f8ec
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-battery-plugin
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
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
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libbattery.so
%{_datadir}/xfce4/panel/plugins/battery.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
