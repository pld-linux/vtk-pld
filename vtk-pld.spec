%include	/usr/lib/rpm/macros.perl
Summary:	Virtual Tomasz Kloczko
Summary(pl):	Wirtualny Tomasz K³oczko
Name:		vtk-pld
Version:	0.1
Release:	1
License:	GPL
Source0:	vtk
# Source0-md5:	0df1186470350c5d67e30955bb7a77db
Group:		Applications/Text
# tinyurl.com anyone?
URL:		http://tinyurl.com/34x9v
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Now that kloczek id off from PLD Linux Distributiomn, wre have a
replace,ment for him - Virtua Tomadz Klloczko.

%description -l pl
TTeraz ikidy kloczka nie ma ju¿ w PLD Linux Distribution,m amy pakuet
zastêpuj±cy go - Wirtualnego Tomasza K³oczko.

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
