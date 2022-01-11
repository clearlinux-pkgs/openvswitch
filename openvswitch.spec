#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : openvswitch
Version  : 2.16.0
Release  : 74
URL      : https://www.openvswitch.org/releases/openvswitch-2.16.0.tar.gz
Source0  : https://www.openvswitch.org/releases/openvswitch-2.16.0.tar.gz
Source1  : openvswitch.service
Summary  : Open vSwitch daemon/database/utilities
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 LGPL-2.1 LGPL-2.1+ SISSL
Requires: openvswitch-bin = %{version}-%{release}
Requires: openvswitch-data = %{version}-%{release}
Requires: openvswitch-license = %{version}-%{release}
Requires: openvswitch-man = %{version}-%{release}
Requires: openvswitch-services = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : groff
BuildRequires : libc-bin
BuildRequires : libcap-ng-dev
BuildRequires : openssl-dev
BuildRequires : pypi(six)
BuildRequires : pypi(sortedcontainers)
BuildRequires : pypi(sphinx)
BuildRequires : pypi-sphinx
BuildRequires : python3-dev
BuildRequires : util-linux
BuildRequires : valgrind

%description
Open vSwitch provides standard network bridging functions augmented with
support for the OpenFlow protocol for remote per-flow control of
traffic.

%package bin
Summary: bin components for the openvswitch package.
Group: Binaries
Requires: openvswitch-data = %{version}-%{release}
Requires: openvswitch-license = %{version}-%{release}
Requires: openvswitch-services = %{version}-%{release}

%description bin
bin components for the openvswitch package.


%package data
Summary: data components for the openvswitch package.
Group: Data

%description data
data components for the openvswitch package.


%package dev
Summary: dev components for the openvswitch package.
Group: Development
Requires: openvswitch-bin = %{version}-%{release}
Requires: openvswitch-data = %{version}-%{release}
Provides: openvswitch-devel = %{version}-%{release}
Requires: openvswitch = %{version}-%{release}

%description dev
dev components for the openvswitch package.


%package extras
Summary: extras components for the openvswitch package.
Group: Default

%description extras
extras components for the openvswitch package.


%package license
Summary: license components for the openvswitch package.
Group: Default

%description license
license components for the openvswitch package.


%package man
Summary: man components for the openvswitch package.
Group: Default

%description man
man components for the openvswitch package.


%package services
Summary: services components for the openvswitch package.
Group: Systemd services

%description services
services components for the openvswitch package.


%package staticdev
Summary: staticdev components for the openvswitch package.
Group: Default
Requires: openvswitch-dev = %{version}-%{release}

%description staticdev
staticdev components for the openvswitch package.


%prep
%setup -q -n openvswitch-2.16.0
cd %{_builddir}/openvswitch-2.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641864661
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1641864661
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openvswitch
cp %{_builddir}/openvswitch-2.16.0/LICENSE %{buildroot}/usr/share/package-licenses/openvswitch/3c434742aa273ef814bb7a58fdb4623df42da007
cp %{_builddir}/openvswitch-2.16.0/NOTICE %{buildroot}/usr/share/package-licenses/openvswitch/d268d05a46cd45e4548e7a3dcc43f16b565a8453
cp %{_builddir}/openvswitch-2.16.0/debian/copyright %{buildroot}/usr/share/package-licenses/openvswitch/21e4c8ae832f888e0ee6b6daa926392867922c5b
cp %{_builddir}/openvswitch-2.16.0/python/ovs/compat/sortedcontainers/LICENSE %{buildroot}/usr/share/package-licenses/openvswitch/e79dc019b36c084ccc00738699f7c50030a3a0b6
cp %{_builddir}/openvswitch-2.16.0/xenserver/LICENSE %{buildroot}/usr/share/package-licenses/openvswitch/58540f918cf80a0242ee25c334f1ff40a7c3fca5
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/openvswitch.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ovs-appctl
/usr/bin/ovs-bugtool
/usr/bin/ovs-dpctl
/usr/bin/ovs-dpctl-top
/usr/bin/ovs-l3ping
/usr/bin/ovs-ofctl
/usr/bin/ovs-parse-backtrace
/usr/bin/ovs-test
/usr/bin/ovs-testcontroller
/usr/bin/ovs-vlan-test
/usr/bin/ovs-vsctl
/usr/bin/ovs-vswitchd
/usr/bin/ovsdb-client
/usr/bin/ovsdb-server
/usr/bin/ovsdb-tool
/usr/bin/vtep-ctl

%files data
%defattr(-,root,root,-)
/usr/share/openvswitch/bugtool-plugins/kernel-info/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/network-status/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/system-logs/openvswitch.xml
/usr/share/openvswitch/scripts/ovs-bugtool-daemons-ver
/usr/share/openvswitch/scripts/ovs-bugtool-fdb-show
/usr/share/openvswitch/scripts/ovs-bugtool-get-dpdk-nic-numa
/usr/share/openvswitch/scripts/ovs-bugtool-get-port-stats
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-appctl-dpif
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-bridge-datapath-type
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-ofctl-loop-over-bridges
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-vswitchd-threads-affinity
/usr/share/openvswitch/scripts/ovs-bugtool-qos-configs
/usr/share/openvswitch/scripts/ovs-bugtool-tc-class-show
/usr/share/openvswitch/scripts/ovs-ctl
/usr/share/openvswitch/scripts/ovs-kmod-ctl
/usr/share/openvswitch/scripts/ovs-lib
/usr/share/openvswitch/scripts/ovs-save
/usr/share/openvswitch/vswitch.ovsschema
/usr/share/openvswitch/vtep.ovsschema

%files dev
%defattr(-,root,root,-)
/usr/include/openflow/intel-ext.h
/usr/include/openflow/netronome-ext.h
/usr/include/openflow/nicira-ext.h
/usr/include/openflow/openflow-1.0.h
/usr/include/openflow/openflow-1.1.h
/usr/include/openflow/openflow-1.2.h
/usr/include/openflow/openflow-1.3.h
/usr/include/openflow/openflow-1.4.h
/usr/include/openflow/openflow-1.5.h
/usr/include/openflow/openflow-common.h
/usr/include/openflow/openflow.h
/usr/include/openvswitch/compiler.h
/usr/include/openvswitch/dynamic-string.h
/usr/include/openvswitch/flow.h
/usr/include/openvswitch/geneve.h
/usr/include/openvswitch/hmap.h
/usr/include/openvswitch/json.h
/usr/include/openvswitch/list.h
/usr/include/openvswitch/match.h
/usr/include/openvswitch/meta-flow.h
/usr/include/openvswitch/namemap.h
/usr/include/openvswitch/netdev.h
/usr/include/openvswitch/nsh.h
/usr/include/openvswitch/ofp-actions.h
/usr/include/openvswitch/ofp-bundle.h
/usr/include/openvswitch/ofp-connection.h
/usr/include/openvswitch/ofp-ed-props.h
/usr/include/openvswitch/ofp-errors.h
/usr/include/openvswitch/ofp-flow.h
/usr/include/openvswitch/ofp-group.h
/usr/include/openvswitch/ofp-ipfix.h
/usr/include/openvswitch/ofp-match.h
/usr/include/openvswitch/ofp-meter.h
/usr/include/openvswitch/ofp-monitor.h
/usr/include/openvswitch/ofp-msgs.h
/usr/include/openvswitch/ofp-packet.h
/usr/include/openvswitch/ofp-parse.h
/usr/include/openvswitch/ofp-port.h
/usr/include/openvswitch/ofp-print.h
/usr/include/openvswitch/ofp-prop.h
/usr/include/openvswitch/ofp-protocol.h
/usr/include/openvswitch/ofp-queue.h
/usr/include/openvswitch/ofp-switch.h
/usr/include/openvswitch/ofp-table.h
/usr/include/openvswitch/ofp-util.h
/usr/include/openvswitch/ofpbuf.h
/usr/include/openvswitch/packets.h
/usr/include/openvswitch/poll-loop.h
/usr/include/openvswitch/rconn.h
/usr/include/openvswitch/shash.h
/usr/include/openvswitch/thread.h
/usr/include/openvswitch/token-bucket.h
/usr/include/openvswitch/tun-metadata.h
/usr/include/openvswitch/type-props.h
/usr/include/openvswitch/types.h
/usr/include/openvswitch/util.h
/usr/include/openvswitch/uuid.h
/usr/include/openvswitch/vconn.h
/usr/include/openvswitch/version.h
/usr/include/openvswitch/vlog.h
/usr/lib64/pkgconfig/libofproto.pc
/usr/lib64/pkgconfig/libopenvswitch.pc
/usr/lib64/pkgconfig/libovsdb.pc
/usr/lib64/pkgconfig/libsflow.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/ovs-docker
/usr/bin/ovs-pcap
/usr/bin/ovs-pki
/usr/bin/ovs-tcpdump
/usr/bin/ovs-tcpundump
/usr/share/openvswitch/python/ovs/__init__.py
/usr/share/openvswitch/python/ovs/compat/__init__.py
/usr/share/openvswitch/python/ovs/compat/sortedcontainers/__init__.py
/usr/share/openvswitch/python/ovs/compat/sortedcontainers/sorteddict.py
/usr/share/openvswitch/python/ovs/compat/sortedcontainers/sortedlist.py
/usr/share/openvswitch/python/ovs/compat/sortedcontainers/sortedset.py
/usr/share/openvswitch/python/ovs/daemon.py
/usr/share/openvswitch/python/ovs/db/__init__.py
/usr/share/openvswitch/python/ovs/db/custom_index.py
/usr/share/openvswitch/python/ovs/db/data.py
/usr/share/openvswitch/python/ovs/db/error.py
/usr/share/openvswitch/python/ovs/db/idl.py
/usr/share/openvswitch/python/ovs/db/parser.py
/usr/share/openvswitch/python/ovs/db/schema.py
/usr/share/openvswitch/python/ovs/db/types.py
/usr/share/openvswitch/python/ovs/dirs.py
/usr/share/openvswitch/python/ovs/fatal_signal.py
/usr/share/openvswitch/python/ovs/fcntl_win.py
/usr/share/openvswitch/python/ovs/json.py
/usr/share/openvswitch/python/ovs/jsonrpc.py
/usr/share/openvswitch/python/ovs/ovsuuid.py
/usr/share/openvswitch/python/ovs/poller.py
/usr/share/openvswitch/python/ovs/process.py
/usr/share/openvswitch/python/ovs/reconnect.py
/usr/share/openvswitch/python/ovs/socket_util.py
/usr/share/openvswitch/python/ovs/stream.py
/usr/share/openvswitch/python/ovs/timeval.py
/usr/share/openvswitch/python/ovs/unixctl/__init__.py
/usr/share/openvswitch/python/ovs/unixctl/client.py
/usr/share/openvswitch/python/ovs/unixctl/server.py
/usr/share/openvswitch/python/ovs/util.py
/usr/share/openvswitch/python/ovs/version.py
/usr/share/openvswitch/python/ovs/vlog.py
/usr/share/openvswitch/python/ovs/winutils.py
/usr/share/openvswitch/python/ovstest/__init__.py
/usr/share/openvswitch/python/ovstest/args.py
/usr/share/openvswitch/python/ovstest/rpcserver.py
/usr/share/openvswitch/python/ovstest/tcp.py
/usr/share/openvswitch/python/ovstest/tests.py
/usr/share/openvswitch/python/ovstest/udp.py
/usr/share/openvswitch/python/ovstest/util.py
/usr/share/openvswitch/python/ovstest/vswitch.py
/usr/share/openvswitch/scripts/ovs-check-dead-ifs
/usr/share/openvswitch/scripts/ovs-monitor-ipsec
/usr/share/openvswitch/scripts/ovs-vtep

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openvswitch/21e4c8ae832f888e0ee6b6daa926392867922c5b
/usr/share/package-licenses/openvswitch/3c434742aa273ef814bb7a58fdb4623df42da007
/usr/share/package-licenses/openvswitch/58540f918cf80a0242ee25c334f1ff40a7c3fca5
/usr/share/package-licenses/openvswitch/d268d05a46cd45e4548e7a3dcc43f16b565a8453
/usr/share/package-licenses/openvswitch/e79dc019b36c084ccc00738699f7c50030a3a0b6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ovs-pcap.1
/usr/share/man/man1/ovs-tcpundump.1
/usr/share/man/man1/ovsdb-client.1
/usr/share/man/man1/ovsdb-server.1
/usr/share/man/man1/ovsdb-tool.1
/usr/share/man/man5/ovs-vswitchd.conf.db.5
/usr/share/man/man5/ovsdb-server.5
/usr/share/man/man5/ovsdb.5
/usr/share/man/man5/vtep.5
/usr/share/man/man7/ovs-actions.7
/usr/share/man/man7/ovs-fields.7
/usr/share/man/man7/ovsdb-server.7
/usr/share/man/man7/ovsdb.7
/usr/share/man/man8/ovs-appctl.8
/usr/share/man/man8/ovs-bugtool.8
/usr/share/man/man8/ovs-ctl.8
/usr/share/man/man8/ovs-dpctl-top.8
/usr/share/man/man8/ovs-dpctl.8
/usr/share/man/man8/ovs-kmod-ctl.8
/usr/share/man/man8/ovs-l3ping.8
/usr/share/man/man8/ovs-ofctl.8
/usr/share/man/man8/ovs-parse-backtrace.8
/usr/share/man/man8/ovs-pki.8
/usr/share/man/man8/ovs-tcpdump.8
/usr/share/man/man8/ovs-test.8
/usr/share/man/man8/ovs-testcontroller.8
/usr/share/man/man8/ovs-vlan-test.8
/usr/share/man/man8/ovs-vsctl.8
/usr/share/man/man8/ovs-vswitchd.8
/usr/share/man/man8/vtep-ctl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/openvswitch.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libofproto.a
/usr/lib64/libopenvswitch.a
/usr/lib64/libopenvswitchavx512.a
/usr/lib64/libovsdb.a
/usr/lib64/libsflow.a
/usr/lib64/libvtep.a
