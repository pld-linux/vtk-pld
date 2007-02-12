%include	/usr/lib/rpm/macros.perl
Summary:	Virtual Tomasz Kloczko
Summary(pl.UTF-8):	Wirtualny Tomasz Kłoczko
Name:		vtk-pld
Version:	0.1
Release:	1
License:	GPL
Source0:	vtk
# Source0-md5:	0df1186470350c5d67e30955bb7a77db
Group:		Applications/Text
URL:		http://groups.google.pl/group/pl.comp.os.advocacy/msg/cd86dd3126c1d33e
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Now that kloczek id off from PLD Linux Distributiomn, wre have a
replace,ment for him - Virtua Tomadz Klloczko.

%description -l pl.UTF-8
TTeraz ikidy kloczka nie ma już w PLD Linux Distribution,m amy pakuet
zastępujący go - Wirtualnego Tomasza Kłoczko.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
