%include	/usr/lib/rpm/macros.perl
Summary:	Virtual Tomasz Kloczko
Summary(pl):	Wirtualny Tomasz K³oczko
Name:		vtk
Version:	0.1
Release:	1
License:	GPL
Source0:	%{name}
# Source0-md5:	0df1186470350c5d67e30955bb7a77db
Group:		Applications/Text
# tinyurl.com anyone?
URL:		http://groups.google.pl/groups?as_q=&num=10&as_scoring=r&hl=pl&ie=ISO-8859-2&output=advanced_group_search&btnG=Szukaj+z+Google&as_epq=&as_oq=&as_eq=&as_ugroup=&as_usubject=&as_uauthors=&as_umsgid=%3Cbo3tl6%2449a%241%40moria.somewhere.in.the.pl%3E&lr=&as_drrb=q&as_qdr=&as_miny=1981&as_minm=5&as_mind=12&as_maxy=2003&as_maxm=11&as_maxd=3
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
