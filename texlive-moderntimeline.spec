# revision 26164
# category Package
# catalog-ctan /macros/latex/contrib/moderntimeline
# catalog-date 2012-01-17 10:30:09 +0100
# catalog-license lppl1.3
# catalog-version 0.6
Name:		texlive-moderntimeline
Version:	0.6
Release:	2
Summary:	Timelines for use with moderncv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moderntimeline
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to configure and to draw time
line diagrams; such diagrams are designed to fit into
Curriculum Vitae documents written using the moderncv class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moderntimeline/moderntimeline.sty
%doc %{_texmfdistdir}/doc/latex/moderntimeline/README
%doc %{_texmfdistdir}/doc/latex/moderntimeline/moderntimeline.pdf
#- source
%doc %{_texmfdistdir}/source/latex/moderntimeline/moderntimeline.dtx
%doc %{_texmfdistdir}/source/latex/moderntimeline/moderntimeline.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
