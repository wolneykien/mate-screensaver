Name: 
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: 
License: GPLv3+
Group: 
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: 

%description

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files

%changelog
