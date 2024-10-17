Name:		texlive-reotex
Version:	34924
Release:	2
Summary:	Draw Reo Channels and Circuits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/reotex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reotex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reotex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines macros and other utilities to design Reo
Circuits. The package require PGF/TikZ support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/reotex/reotex.sty
%doc %{_texmfdistdir}/doc/latex/reotex/README
%doc %{_texmfdistdir}/doc/latex/reotex/reotex.pdf
%doc %{_texmfdistdir}/doc/latex/reotex/reotex.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
