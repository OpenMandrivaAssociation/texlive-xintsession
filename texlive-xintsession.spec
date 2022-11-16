Name:		texlive-xintsession
Version:	60926
Release:	1
Summary:	Interactive computing sessions (fractions, floating points, polynomials)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xintsession
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xintsession.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xintsession.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for interactive computing
sessions with etex (or pdftex) executed on the command line, on
the basis of the xintexpr and polexpr packages. Once
xintsession is loaded, eTeX becomes an interactive computing
software capable of executing arbitrary precision calculations,
or exact calculations with arbitrarily big fractions. It can
also manipulate polynomials as algebraic entities. Numerical
variables and functions can be defined during the session, and
each evaluation result is stored in automatically labeled
variables. A file is automatically created storing inputs and
outputs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/xintsession
%doc %{_texmfdistdir}/doc/plain/xintsession

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
