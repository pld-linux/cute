Summary:	CUTE User-friendly Text Editor
Summary(pl):	CUTE - przyjazny dla u¿ytkownika edytor tekstu
Name:		cute
Version:	0.2.7
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/cute/%{name}-%{version}-1.tar.gz
# Source0-md5:	4b7d088781ecb42944554e3c051af78c
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	python-devel
BuildRequires:	qscintilla-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CUTE is a Qt and Scintilla based text editor which can be easily
extended using Python. Its main purpose is to be an user-friendly
source code editor with a common graphical user interface. The editor
supports syntax highlighting for many languages, tags files and
projects.

%description -l pl
CUTE to oparty na Qt i Scintilli edytor tekstu, który mo¿na ³atwo
rozszerzaæ przy u¿yciu Pythona. G³ównym jego celem jest bycie
przyjaznym dla u¿ytkownia edytorem kodu ¼ród³owego ze wspólnym
graficznym interfejsem u¿ytkownika. Edytor obs³uguje pod¶wietlanie
sk³adni dla wielu jêzyków, pliki znaczników oraz projekty.

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
