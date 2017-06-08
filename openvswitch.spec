#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openvswitch
Version  : 2.6.1
Release  : 34
URL      : http://openvswitch.org/releases/openvswitch-2.6.1.tar.gz
Source0  : http://openvswitch.org/releases/openvswitch-2.6.1.tar.gz
Source1  : openvswitch.service
Summary  : Open vSwitch daemon/database/utilities
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 LGPL-2.1 LGPL-2.1+ SISSL
Requires: openvswitch-bin
Requires: openvswitch-config
Requires: openvswitch-doc
Requires: openvswitch-data
BuildRequires : dpdk-dev
BuildRequires : groff
BuildRequires : libc-bin
BuildRequires : libcap-ng-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: cve-2017-9264.patch

%description
Open vSwitch provides standard network bridging functions and
support for the OpenFlow protocol for remote per-flow control of
traffic.

%package bin
Summary: bin components for the openvswitch package.
Group: Binaries
Requires: openvswitch-data
Requires: openvswitch-config

%description bin
bin components for the openvswitch package.


%package config
Summary: config components for the openvswitch package.
Group: Default

%description config
config components for the openvswitch package.


%package data
Summary: data components for the openvswitch package.
Group: Data

%description data
data components for the openvswitch package.


%package dev
Summary: dev components for the openvswitch package.
Group: Development
Requires: openvswitch-bin
Requires: openvswitch-data
Provides: openvswitch-devel

%description dev
dev components for the openvswitch package.


%package doc
Summary: doc components for the openvswitch package.
Group: Documentation

%description doc
doc components for the openvswitch package.


%prep
%setup -q -n openvswitch-2.6.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496961185
unset LD_AS_NEEDED
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static --with-dpdk=/usr/share/dpdk/x86_64-native-linuxapp-gcc/
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1496961185
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/openvswitch.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ovn-controller
/usr/bin/ovn-controller-vtep
/usr/bin/ovn-docker-overlay-driver
/usr/bin/ovn-docker-underlay-driver
/usr/bin/ovn-nbctl
/usr/bin/ovn-northd
/usr/bin/ovn-sbctl
/usr/bin/ovn-trace
/usr/bin/ovs-appctl
/usr/bin/ovs-bugtool
/usr/bin/ovs-docker
/usr/bin/ovs-dpctl
/usr/bin/ovs-dpctl-top
/usr/bin/ovs-l3ping
/usr/bin/ovs-ofctl
/usr/bin/ovs-parse-backtrace
/usr/bin/ovs-pcap
/usr/bin/ovs-pki
/usr/bin/ovs-tcpdump
/usr/bin/ovs-tcpundump
/usr/bin/ovs-test
/usr/bin/ovs-testcontroller
/usr/bin/ovs-vlan-bug-workaround
/usr/bin/ovs-vlan-test
/usr/bin/ovs-vsctl
/usr/bin/ovs-vswitchd
/usr/bin/ovsdb-client
/usr/bin/ovsdb-server
/usr/bin/ovsdb-tool
/usr/bin/vtep-ctl

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/openvswitch.service

%files data
%defattr(-,root,root,-)
/usr/share/openvswitch/bugtool-plugins/kernel-info/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/network-status/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/network-status/ovn.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/system-logs/openvswitch.xml
/usr/share/openvswitch/ovn-nb.ovsschema
/usr/share/openvswitch/ovn-sb.ovsschema
/usr/share/openvswitch/python/ovs/__init__.py
/usr/share/openvswitch/python/ovs/__init__.pyc
/usr/share/openvswitch/python/ovs/__init__.pyo
/usr/share/openvswitch/python/ovs/daemon.py
/usr/share/openvswitch/python/ovs/daemon.pyc
/usr/share/openvswitch/python/ovs/daemon.pyo
/usr/share/openvswitch/python/ovs/db/__init__.py
/usr/share/openvswitch/python/ovs/db/__init__.pyc
/usr/share/openvswitch/python/ovs/db/__init__.pyo
/usr/share/openvswitch/python/ovs/db/data.py
/usr/share/openvswitch/python/ovs/db/data.pyc
/usr/share/openvswitch/python/ovs/db/data.pyo
/usr/share/openvswitch/python/ovs/db/error.py
/usr/share/openvswitch/python/ovs/db/error.pyc
/usr/share/openvswitch/python/ovs/db/error.pyo
/usr/share/openvswitch/python/ovs/db/idl.py
/usr/share/openvswitch/python/ovs/db/idl.pyc
/usr/share/openvswitch/python/ovs/db/idl.pyo
/usr/share/openvswitch/python/ovs/db/parser.py
/usr/share/openvswitch/python/ovs/db/parser.pyc
/usr/share/openvswitch/python/ovs/db/parser.pyo
/usr/share/openvswitch/python/ovs/db/schema.py
/usr/share/openvswitch/python/ovs/db/schema.pyc
/usr/share/openvswitch/python/ovs/db/schema.pyo
/usr/share/openvswitch/python/ovs/db/types.py
/usr/share/openvswitch/python/ovs/db/types.pyc
/usr/share/openvswitch/python/ovs/db/types.pyo
/usr/share/openvswitch/python/ovs/dirs.py
/usr/share/openvswitch/python/ovs/dirs.pyc
/usr/share/openvswitch/python/ovs/dirs.pyo
/usr/share/openvswitch/python/ovs/fatal_signal.py
/usr/share/openvswitch/python/ovs/fatal_signal.pyc
/usr/share/openvswitch/python/ovs/fatal_signal.pyo
/usr/share/openvswitch/python/ovs/fcntl_win.py
/usr/share/openvswitch/python/ovs/fcntl_win.pyc
/usr/share/openvswitch/python/ovs/fcntl_win.pyo
/usr/share/openvswitch/python/ovs/json.py
/usr/share/openvswitch/python/ovs/json.pyc
/usr/share/openvswitch/python/ovs/json.pyo
/usr/share/openvswitch/python/ovs/jsonrpc.py
/usr/share/openvswitch/python/ovs/jsonrpc.pyc
/usr/share/openvswitch/python/ovs/jsonrpc.pyo
/usr/share/openvswitch/python/ovs/ovsuuid.py
/usr/share/openvswitch/python/ovs/ovsuuid.pyc
/usr/share/openvswitch/python/ovs/ovsuuid.pyo
/usr/share/openvswitch/python/ovs/poller.py
/usr/share/openvswitch/python/ovs/poller.pyc
/usr/share/openvswitch/python/ovs/poller.pyo
/usr/share/openvswitch/python/ovs/process.py
/usr/share/openvswitch/python/ovs/process.pyc
/usr/share/openvswitch/python/ovs/process.pyo
/usr/share/openvswitch/python/ovs/reconnect.py
/usr/share/openvswitch/python/ovs/reconnect.pyc
/usr/share/openvswitch/python/ovs/reconnect.pyo
/usr/share/openvswitch/python/ovs/socket_util.py
/usr/share/openvswitch/python/ovs/socket_util.pyc
/usr/share/openvswitch/python/ovs/socket_util.pyo
/usr/share/openvswitch/python/ovs/stream.py
/usr/share/openvswitch/python/ovs/stream.pyc
/usr/share/openvswitch/python/ovs/stream.pyo
/usr/share/openvswitch/python/ovs/timeval.py
/usr/share/openvswitch/python/ovs/timeval.pyc
/usr/share/openvswitch/python/ovs/timeval.pyo
/usr/share/openvswitch/python/ovs/unixctl/__init__.py
/usr/share/openvswitch/python/ovs/unixctl/__init__.pyc
/usr/share/openvswitch/python/ovs/unixctl/__init__.pyo
/usr/share/openvswitch/python/ovs/unixctl/client.py
/usr/share/openvswitch/python/ovs/unixctl/client.pyc
/usr/share/openvswitch/python/ovs/unixctl/client.pyo
/usr/share/openvswitch/python/ovs/unixctl/server.py
/usr/share/openvswitch/python/ovs/unixctl/server.pyc
/usr/share/openvswitch/python/ovs/unixctl/server.pyo
/usr/share/openvswitch/python/ovs/util.py
/usr/share/openvswitch/python/ovs/util.pyc
/usr/share/openvswitch/python/ovs/util.pyo
/usr/share/openvswitch/python/ovs/version.py
/usr/share/openvswitch/python/ovs/version.pyc
/usr/share/openvswitch/python/ovs/version.pyo
/usr/share/openvswitch/python/ovs/vlog.py
/usr/share/openvswitch/python/ovs/vlog.pyc
/usr/share/openvswitch/python/ovs/vlog.pyo
/usr/share/openvswitch/python/ovstest/__init__.py
/usr/share/openvswitch/python/ovstest/__init__.pyc
/usr/share/openvswitch/python/ovstest/__init__.pyo
/usr/share/openvswitch/python/ovstest/args.py
/usr/share/openvswitch/python/ovstest/args.pyc
/usr/share/openvswitch/python/ovstest/args.pyo
/usr/share/openvswitch/python/ovstest/rpcserver.py
/usr/share/openvswitch/python/ovstest/rpcserver.pyc
/usr/share/openvswitch/python/ovstest/rpcserver.pyo
/usr/share/openvswitch/python/ovstest/tcp.py
/usr/share/openvswitch/python/ovstest/tcp.pyc
/usr/share/openvswitch/python/ovstest/tcp.pyo
/usr/share/openvswitch/python/ovstest/tests.py
/usr/share/openvswitch/python/ovstest/tests.pyc
/usr/share/openvswitch/python/ovstest/tests.pyo
/usr/share/openvswitch/python/ovstest/udp.py
/usr/share/openvswitch/python/ovstest/udp.pyc
/usr/share/openvswitch/python/ovstest/udp.pyo
/usr/share/openvswitch/python/ovstest/util.py
/usr/share/openvswitch/python/ovstest/util.pyc
/usr/share/openvswitch/python/ovstest/util.pyo
/usr/share/openvswitch/python/ovstest/vswitch.py
/usr/share/openvswitch/python/ovstest/vswitch.pyc
/usr/share/openvswitch/python/ovstest/vswitch.pyo
/usr/share/openvswitch/scripts/ovn-bugtool-nbctl-show
/usr/share/openvswitch/scripts/ovn-bugtool-sbctl-lflow-list
/usr/share/openvswitch/scripts/ovn-bugtool-sbctl-show
/usr/share/openvswitch/scripts/ovn-ctl
/usr/share/openvswitch/scripts/ovs-bugtool-bfd-show
/usr/share/openvswitch/scripts/ovs-bugtool-bond-show
/usr/share/openvswitch/scripts/ovs-bugtool-cfm-show
/usr/share/openvswitch/scripts/ovs-bugtool-conntrack-dump
/usr/share/openvswitch/scripts/ovs-bugtool-coverage-show
/usr/share/openvswitch/scripts/ovs-bugtool-daemons-ver
/usr/share/openvswitch/scripts/ovs-bugtool-fdb-show
/usr/share/openvswitch/scripts/ovs-bugtool-lacp-show
/usr/share/openvswitch/scripts/ovs-bugtool-list-dbs
/usr/share/openvswitch/scripts/ovs-bugtool-memory-show
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-appctl-dpif
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-ofctl-dump-flows
/usr/share/openvswitch/scripts/ovs-bugtool-ovs-ofctl-show
/usr/share/openvswitch/scripts/ovs-bugtool-ovsdb-dump
/usr/share/openvswitch/scripts/ovs-bugtool-tc-class-show
/usr/share/openvswitch/scripts/ovs-bugtool-vsctl-show
/usr/share/openvswitch/scripts/ovs-check-dead-ifs
/usr/share/openvswitch/scripts/ovs-ctl
/usr/share/openvswitch/scripts/ovs-lib
/usr/share/openvswitch/scripts/ovs-save
/usr/share/openvswitch/scripts/ovs-vtep
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
/usr/include/openvswitch/netdev.h
/usr/include/openvswitch/ofp-actions.h
/usr/include/openvswitch/ofp-errors.h
/usr/include/openvswitch/ofp-msgs.h
/usr/include/openvswitch/ofp-parse.h
/usr/include/openvswitch/ofp-print.h
/usr/include/openvswitch/ofp-prop.h
/usr/include/openvswitch/ofp-util.h
/usr/include/openvswitch/ofpbuf.h
/usr/include/openvswitch/packets.h
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
/usr/include/ovn/actions.h
/usr/include/ovn/expr.h
/usr/include/ovn/lex.h
/usr/lib64/pkgconfig/libofproto.pc
/usr/lib64/pkgconfig/libopenvswitch.pc
/usr/lib64/pkgconfig/libovsdb.pc
/usr/lib64/pkgconfig/libsflow.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*
