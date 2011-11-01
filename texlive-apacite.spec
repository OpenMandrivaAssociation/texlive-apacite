Name:		texlive-apacite
Version:	4.05
Release:	1
Summary:	Citation style following the rules of the APA
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/apacite
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apacite.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Apacite is a BibTeX style which closely follows American
Psychological Association style citations, providing a very
good match. The package follows the the 5th edition of the APA
manual, and provides up to date documentation and a test
document. The package is compatible with chapterbib and (to
some extent) with hyperref (for limits of compatibility, see
the manual). The package also includes a means of generating an
author index for a document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%doc %{_texmfdistdir}/doc/latex/apacite/README
%doc %{_texmfdistdir}/doc/latex/apacite/apa5ex.bib
%doc %{_texmfdistdir}/doc/latex/apacite/apacite.pdf
#- source
%doc %{_texmfdistdir}/source/latex/apacite/apacite.drv
%doc %{_texmfdistdir}/source/latex/apacite/apacite.dtx
%doc %{_texmfdistdir}/source/latex/apacite/apacite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}