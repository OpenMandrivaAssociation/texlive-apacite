Name:		texlive-apacite
Version:	54080
Release:	1
Summary:	Citation style following the rules of the APA
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/apacite
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Apacite provides a BibTeX style and a LaTeX package which are
designed to match the requirements of the American
Psychological Association's style for citations. The package
follows the 6th edition of the APA manual, and is designed to
work with the apa6 class. A test document is provided. The
package is compatible with chapterbib and (to some extent) with
hyperref (for limits of compatibility, see the documentation).
The package also includes a means of generating an author index
for a document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/apacite/apacann.bst
%{_texmfdistdir}/bibtex/bst/apacite/apacannx.bst
%{_texmfdistdir}/bibtex/bst/apacite/apacite.bst
%{_texmfdistdir}/bibtex/bst/apacite/apacitex.bst
%{_texmfdistdir}/tex/latex/apacite/apacdoc.sty
%{_texmfdistdir}/tex/latex/apacite/apacite.sty
%{_texmfdistdir}/tex/latex/apacite/dutch.apc
%{_texmfdistdir}/tex/latex/apacite/english.apc
%{_texmfdistdir}/tex/latex/apacite/finnish.apc
%{_texmfdistdir}/tex/latex/apacite/french.apc
%{_texmfdistdir}/tex/latex/apacite/german.apc
%{_texmfdistdir}/tex/latex/apacite/greek.apc
%{_texmfdistdir}/tex/latex/apacite/ngerman.apc
%{_texmfdistdir}/tex/latex/apacite/norsk.apc
%{_texmfdistdir}/tex/latex/apacite/spanish.apc
%{_texmfdistdir}/tex/latex/apacite/swedish.apc
%doc %{_texmfdistdir}/doc/bibtex/apacite/README
%doc %{_texmfdistdir}/doc/bibtex/apacite/apa5ex.bib
%doc %{_texmfdistdir}/doc/bibtex/apacite/apacite.pdf
%doc %{_texmfdistdir}/doc/bibtex/apacite/apacxmpl.tex
#- source
%doc %{_texmfdistdir}/source/bibtex/apacite/apacite.drv
%doc %{_texmfdistdir}/source/bibtex/apacite/apacite.dtx
%doc %{_texmfdistdir}/source/bibtex/apacite/apacite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
