Name:		texlive-moderntimeline
Version:	55518
Release:	2
Summary:	Timelines for use with moderncv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moderntimeline
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/moderntimeline
%doc %{_texmfdistdir}/doc/latex/moderntimeline
#- source
%doc %{_texmfdistdir}/source/latex/moderntimeline

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
