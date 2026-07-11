%global tl_name moderntimeline
%global tl_revision 55518

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Timelines for use with moderncv
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moderntimeline
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moderntimeline.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to configure and to draw time line
diagrams; such diagrams are designed to fit into Curriculum Vitae
documents written using the moderncv class.

