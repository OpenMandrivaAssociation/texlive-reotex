# revision 29803
# category Package
# catalog-ctan /graphics/pgf/contrib/reotex
# catalog-date 2012-01-11 08:56:14 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-reotex
Version:	1.0
Release:	2
Summary:	Draw Reo Channels and Circuits
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/reotex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reotex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reotex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
