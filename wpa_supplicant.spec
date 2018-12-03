#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2B6EF432EFC895FA (j@w1.fi)
#
Name     : wpa_supplicant
Version  : 2.7
Release  : 28
URL      : http://w1.fi/releases/wpa_supplicant-2.7.tar.gz
Source0  : http://w1.fi/releases/wpa_supplicant-2.7.tar.gz
Source1  : wpa_supplicant.service
Source99 : http://w1.fi/releases/wpa_supplicant-2.7.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: wpa_supplicant-bin = %{version}-%{release}
Requires: wpa_supplicant-data = %{version}-%{release}
Requires: wpa_supplicant-license = %{version}-%{release}
Requires: wpa_supplicant-services = %{version}-%{release}
Requires: linux-firmware-wifi
BuildRequires : buildreq-qmake
BuildRequires : dbus-dev
BuildRequires : libnl-dev
BuildRequires : openssl-dev
Patch1: config.patch
Patch2: CVE-2017-13077.nopatch
Patch3: CVE-2017-13078.nopatch
Patch4: CVE-2017-13079.nopatch
Patch5: CVE-2017-13080.nopatch
Patch6: CVE-2017-13081.nopatch
Patch7: CVE-2017-13082.nopatch
Patch8: CVE-2017-13084.nopatch
Patch9: CVE-2017-13086.nopatch
Patch10: CVE-2017-13087.nopatch
Patch11: CVE-2017-13088.nopatch

%description
wpa_supplicant and hostapd
--------------------------
All Rights Reserved.
These programs are licensed under the BSD license (the one with
advertisement clause removed).

%package bin
Summary: bin components for the wpa_supplicant package.
Group: Binaries
Requires: wpa_supplicant-data = %{version}-%{release}
Requires: wpa_supplicant-license = %{version}-%{release}
Requires: wpa_supplicant-services = %{version}-%{release}

%description bin
bin components for the wpa_supplicant package.


%package data
Summary: data components for the wpa_supplicant package.
Group: Data

%description data
data components for the wpa_supplicant package.


%package license
Summary: license components for the wpa_supplicant package.
Group: Default

%description license
license components for the wpa_supplicant package.


%package services
Summary: services components for the wpa_supplicant package.
Group: Systemd services

%description services
services components for the wpa_supplicant package.


%prep
%setup -q -n wpa_supplicant-2.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543817724
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
pushd wpa_supplicant
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1543817724
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wpa_supplicant
cp COPYING %{buildroot}/usr/share/package-licenses/wpa_supplicant/COPYING
pushd wpa_supplicant
%make_install
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/wpa_supplicant.service
## install_append content
chmod -x %{buildroot}/usr/lib/systemd/system/*
mkdir -p %{buildroot}/usr/share/dbus-1/system-services/
install -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service %{buildroot}/usr/share/dbus-1/system-services/
install -m 0644 wpa_supplicant/dbus/fi.epitest.hostap.WPASupplicant.service %{buildroot}/usr/share/dbus-1/system-services/
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
install -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf %{buildroot}/usr/share/dbus-1/system.d/wpa_supplicant.conf
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wpa_cli
/usr/bin/wpa_passphrase
/usr/bin/wpa_supplicant

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service
/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service
/usr/share/dbus-1/system.d/wpa_supplicant.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wpa_supplicant/COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/wpa_supplicant-nl80211@.service
/usr/lib/systemd/system/wpa_supplicant-wired@.service
/usr/lib/systemd/system/wpa_supplicant.service
/usr/lib/systemd/system/wpa_supplicant@.service
