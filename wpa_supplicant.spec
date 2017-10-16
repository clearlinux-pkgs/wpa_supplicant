#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2B6EF432EFC895FA (j@w1.fi)
#
Name     : wpa_supplicant
Version  : 2.6
Release  : 21
URL      : http://w1.fi/releases/wpa_supplicant-2.6.tar.gz
Source0  : http://w1.fi/releases/wpa_supplicant-2.6.tar.gz
Source1  : wpa_supplicant.service
Source99 : http://w1.fi/releases/wpa_supplicant-2.6.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: wpa_supplicant-bin
Requires: wpa_supplicant-config
Requires: wpa_supplicant-data
BuildRequires : dbus-dev
BuildRequires : libnl-dev
BuildRequires : openssl-dev
Patch1: config.patch
Patch2: rebased-v2.6-0001-hostapd-Avoid-key-reinstallation-in-FT-handshake.patch
Patch3: rebased-v2.6-0002-Prevent-reinstallation-of-an-already-in-use-group-ke.patch
Patch4: rebased-v2.6-0003-Extend-protection-of-GTK-IGTK-reinstallation-of-WNM-.patch
Patch5: rebased-v2.6-0004-Prevent-installation-of-an-all-zero-TK.patch
Patch6: rebased-v2.6-0005-Fix-PTK-rekeying-to-generate-a-new-ANonce.patch
Patch7: rebased-v2.6-0006-TDLS-Reject-TPK-TK-reconfiguration.patch
Patch8: rebased-v2.6-0007-WNM-Ignore-WNM-Sleep-Mode-Response-without-pending-r.patch
Patch9: rebased-v2.6-0008-FT-Do-not-allow-multiple-Reassociation-Response-fram.patch

%description
wpa_supplicant and hostapd
--------------------------
All Rights Reserved.
These programs are licensed under the BSD license (the one with
advertisement clause removed).

%package bin
Summary: bin components for the wpa_supplicant package.
Group: Binaries
Requires: wpa_supplicant-data
Requires: wpa_supplicant-config

%description bin
bin components for the wpa_supplicant package.


%package config
Summary: config components for the wpa_supplicant package.
Group: Default

%description config
config components for the wpa_supplicant package.


%package data
Summary: data components for the wpa_supplicant package.
Group: Data

%description data
data components for the wpa_supplicant package.


%prep
%setup -q -n wpa_supplicant-2.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508173323
pushd wpa_supplicant
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1508173323
rm -rf %{buildroot}
pushd wpa_supplicant
%make_install
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/wpa_supplicant.service
## make_install_append content
chmod -x %{buildroot}/usr/lib/systemd/system/*
mkdir -p %{buildroot}/usr/share/dbus-1/system-services/
install -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service %{buildroot}/usr/share/dbus-1/system-services/
install -m 0644 wpa_supplicant/dbus/fi.epitest.hostap.WPASupplicant.service %{buildroot}/usr/share/dbus-1/system-services/
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
install -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf %{buildroot}/usr/share/dbus-1/system.d/wpa_supplicant.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wpa_cli
/usr/bin/wpa_passphrase
/usr/bin/wpa_supplicant

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/wpa_supplicant-nl80211@.service
/usr/lib/systemd/system/wpa_supplicant-wired@.service
/usr/lib/systemd/system/wpa_supplicant.service
/usr/lib/systemd/system/wpa_supplicant@.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service
/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service
/usr/share/dbus-1/system.d/wpa_supplicant.conf
