Summary:	ecleTeX - plugin for Eclipse
Summary(pl):	ecleTeX - wtyczka do ¶rodowiska Eclipse
Name:		eclipse-plugin-ecleTeX
Version:	0.0.4
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/etex/ecletex.%{version}.zip
# Source0-md5:	9c8da13bbcbe35914a8932d1af78b8da
URL:		http://etex.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir  	%{_libdir}/eclipse

%description
ecleTeX is a LaTeX environment plugin for the Eclipse platform. It
currently supports LaTeX project types, a multilanguage spellchecker,
code highlighting, code completion, Build engines for LaTeX, bibtex,
PDF and PS, a Bibtex view and a basic DVI viewer.

%description -l pl
ecleTeX jest wtyczk± ¶rodowiska LaTeX dla platformy Eclipse. Obecnie
obs³uguje projekty LaTeXa, sprawdzanie pisowni w wielu jêzykach,
pod¶wietlanie sk³adni, dope³nianie kodu, silniki budowania dla LaTeXa,
bibtexa, PDF i PS, przegl±darkê Bibtexa i prost± przegl±darkê DVI.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

cp -r * $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/*
