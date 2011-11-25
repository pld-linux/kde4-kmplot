%define		_state		stable
%define		orgname		kmplot

Summary:	K Desktop Environment - Mathematical function plotter
Summary(pl_PL.UTF8):	K Desktop Environment - Rysowanie wykresów funkcji matematycznych
Name:		kmplot
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	5eec907bdce49c2b738283d017cea3dc
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-kmplot < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description -l pl.UTF-8
KmPlot to narzędzie do rysowania wykresów funkcji matematycznych dla
środowiska KDE. Ma wbudowany potężny parser. Można rysować różne
funkcje jednocześnie i łączyć je, aby stworzyć nowe funkcje.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%attr(755,root,root) %{_libdir}/kde4/libkmplotpart.so
%{_datadir}/apps/kmplot
%{_datadir}/config.kcfg/kmplot.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.View.xml
%{_datadir}/kde4/services/kmplot_part.desktop
%{_desktopdir}/kde4/kmplot.desktop
%{_iconsdir}/hicolor/scalable/apps/kmplot.svgz
%{_iconsdir}/hicolor/*x*/apps/kmplot.png
%{_mandir}/man1/kmplot.1*
