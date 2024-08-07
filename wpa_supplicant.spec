#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v16
# autospec commit: 1bec16f
#
# Source0 file verified with key 0x2B6EF432EFC895FA (j@w1.fi)
#
Name     : wpa_supplicant
Version  : 2.11
Release  : 43
URL      : https://w1.fi/releases/wpa_supplicant-2.11.tar.gz
Source0  : https://w1.fi/releases/wpa_supplicant-2.11.tar.gz
Source1  : wpa_supplicant.service
Source2  : https://w1.fi/releases/wpa_supplicant-2.11.tar.gz.asc
Source3  : 2B6EF432EFC895FA.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: wpa_supplicant-bin = %{version}-%{release}
Requires: wpa_supplicant-data = %{version}-%{release}
Requires: wpa_supplicant-license = %{version}-%{release}
Requires: wpa_supplicant-services = %{version}-%{release}
BuildRequires : dbus-dev
BuildRequires : gnupg
BuildRequires : libnl-dev
BuildRequires : openssl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-configuration-options-and-service-to-install.patch

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
Requires: systemd

%description services
services components for the wpa_supplicant package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE3}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE2} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2B6EF432EFC895FA' gpg.status
%setup -q -n wpa_supplicant-2.11
cd %{_builddir}/wpa_supplicant-2.11
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721671798
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd wpa_supplicant
export GOAMD64=v2
make  %{?_smp_mflags}
popd


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721671798
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wpa_supplicant
cp %{_builddir}/wpa_supplicant-%{version}/COPYING %{buildroot}/usr/share/package-licenses/wpa_supplicant/704ec0c10de3548c062e643e012f0ee4ead22bd5 || :
export GOAMD64=v2
pushd wpa_supplicant
GOAMD64=v2
%make_install
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/wpa_supplicant.service
## install_append content
chmod -x %{buildroot}/usr/lib/systemd/system/*
mkdir -p %{buildroot}/usr/share/dbus-1/system-services/
install -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service %{buildroot}/usr/share/dbus-1/system-services/
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
/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service
/usr/share/dbus-1/system.d/wpa_supplicant.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wpa_supplicant/704ec0c10de3548c062e643e012f0ee4ead22bd5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/wpa_supplicant-nl80211@.service
/usr/lib/systemd/system/wpa_supplicant-wired@.service
/usr/lib/systemd/system/wpa_supplicant.service
/usr/lib/systemd/system/wpa_supplicant@.service
