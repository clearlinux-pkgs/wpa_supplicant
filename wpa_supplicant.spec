#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wpa_supplicant
Version  : 2.4
Release  : 5
URL      : http://w1.fi/releases/wpa_supplicant-2.4.tar.gz
Source0  : http://w1.fi/releases/wpa_supplicant-2.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: wpa_supplicant-bin
Requires: wpa_supplicant-config
BuildRequires : libnl-dev
BuildRequires : openssl-dev
Patch1: config.patch
Patch2: CVE-2015-1863.patch
Patch3: CVE-2015-4141.patch
Patch4: CVE-2015-4142.patch
Patch5: CVE-2015-4143.patch
Patch6: CVE-2015-4144.patch
Patch7: CVE-2015-4145.patch
Patch8: CVE-2015-4146.patch
Patch9: CVE-2015-4146-2.patch

%description
wpa_supplicant and hostapd
--------------------------
All Rights Reserved.
These programs are licensed under the BSD license (the one with
advertisement clause removed).

%package bin
Summary: bin components for the wpa_supplicant package.
Group: Binaries
Requires: wpa_supplicant-config

%description bin
bin components for the wpa_supplicant package.


%package config
Summary: config components for the wpa_supplicant package.
Group: Default

%description config
config components for the wpa_supplicant package.


%prep
%setup -q -n wpa_supplicant-2.4
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
pushd wpa_supplicant
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
pushd wpa_supplicant
%make_install
popd

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
