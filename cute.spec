Summary:	CUTE User-friendly Text Editor
Summary(pl.UTF-8):   CUTE - przyjazny dla użytkownika edytor tekstu
Name:		cute
Version:	0.2.9
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/cute/%{name}-%{version}.tar.gz
# Source0-md5:	08da2882c51f2199ac0812a3500ddec6
URL:		http://cute.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	python-devel
BuildRequires:	qscintilla-devel
BuildRequires:	sed >= 4.0
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CUTE is a Qt and Scintilla based text editor which can be easily
extended using Python. Its main purpose is to be an user-friendly
source code editor with a common graphical user interface. The editor
supports syntax highlighting for many languages, tags files and
projects.

%description -l pl.UTF-8
CUTE to oparty na Qt i Scintilli edytor tekstu, który można łatwo
rozszerzać przy użyciu Pythona. Głównym jego celem jest bycie
przyjaznym dla użytkownika edytorem kodu źródłowego ze wspólnym
graficznym interfejsem użytkownika. Edytor obsługuje podświetlanie
składni dla wielu języków, pliki znaczników oraz projekty.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++/"
rm -rf qscintilla
cd cute
sed -i -e 's#^PYTHON_INCLUDE_DIR.*=.*#PYTHON_INCLUDE_DIR = %{py_incdir}#g' cute.pro
sed -i -e 's#^PYTHON_LIB_DIR.*=.*#PYTHON_LIB_DIR = %{py_libdir}#g' cute.pro
sed -i -e 's#^QEXTSCINTILLADIR.*=.*#QEXTSCINTILLADIR = %{_includedir}#g' cute.pro
sed -i -e 's#-lpython2.2#-lpython#g' cute.pro
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_datadir}/%{name}/{langs,lib/scripts}}

cd cute
install ../bin/cute $RPM_BUILD_ROOT%{_bindir}
install langs/*.* $RPM_BUILD_ROOT%{_datadir}/%{name}/langs
install scripts/*.* $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/scripts
install icons/cute.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc cute/doc/doc cute/cute-api
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*.*
