#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openvswitch
Version  : 2.8.1
Release  : 52
URL      : http://openvswitch.org/releases/openvswitch-2.8.1.tar.gz
Source0  : http://openvswitch.org/releases/openvswitch-2.8.1.tar.gz
Source1  : openvswitch.service
Summary  : Open vSwitch Kernel Modules
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 LGPL-2.1 LGPL-2.1+ SISSL
Requires: openvswitch-bin
Requires: openvswitch-config
Requires: openvswitch-license
Requires: openvswitch-man
Requires: openvswitch-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-distutils3
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libc-bin
BuildRequires : libcap-ng-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : openssl-dev
BuildRequires : pkg-config-dev
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : six-legacypython
BuildRequires : valgrind
Patch1: build.patch

%description
Open vSwitch provides standard network bridging functions augmented with
support for the OpenFlow protocol for remote per-flow control of
traffic. This package contains the kernel modules.

%package bin
Summary: bin components for the openvswitch package.
Group: Binaries
Requires: openvswitch-data
Requires: openvswitch-config
Requires: openvswitch-license
Requires: openvswitch-man

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
Requires: openvswitch-man

%description doc
doc components for the openvswitch package.


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


%prep
%setup -q -n openvswitch-2.8.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532467430
unset LD_AS_NEEDED
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1532467430
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openvswitch
cp COPYING %{buildroot}/usr/share/doc/openvswitch/COPYING
cp NOTICE %{buildroot}/usr/share/doc/openvswitch/NOTICE
cp debian/copyright %{buildroot}/usr/share/doc/openvswitch/debian_copyright
cp xenserver/LICENSE %{buildroot}/usr/share/doc/openvswitch/xenserver_LICENSE
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/openvswitch.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/ovn-detrace
%exclude /usr/bin/ovn-docker-overlay-driver
%exclude /usr/bin/ovn-docker-underlay-driver
%exclude /usr/bin/ovs-bugtool
%exclude /usr/bin/ovs-dpctl-top
%exclude /usr/bin/ovs-l3ping
%exclude /usr/bin/ovs-parse-backtrace
%exclude /usr/bin/ovs-pcap
%exclude /usr/bin/ovs-tcpdump
%exclude /usr/bin/ovs-tcpundump
%exclude /usr/bin/ovs-test
%exclude /usr/bin/ovs-vlan-test
/usr/bin/ovn-controller
/usr/bin/ovn-controller-vtep
/usr/bin/ovn-nbctl
/usr/bin/ovn-northd
/usr/bin/ovn-sbctl
/usr/bin/ovn-trace
/usr/bin/ovs-appctl
/usr/bin/ovs-docker
/usr/bin/ovs-dpctl
/usr/bin/ovs-ofctl
/usr/bin/ovs-pki
/usr/bin/ovs-testcontroller
/usr/bin/ovs-vlan-bug-workaround
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
%exclude /usr/share/openvswitch/python/ovs/__init__.py
%exclude /usr/share/openvswitch/python/ovs/daemon.py
%exclude /usr/share/openvswitch/python/ovs/db/__init__.py
%exclude /usr/share/openvswitch/python/ovs/db/data.py
%exclude /usr/share/openvswitch/python/ovs/db/error.py
%exclude /usr/share/openvswitch/python/ovs/db/idl.py
%exclude /usr/share/openvswitch/python/ovs/db/parser.py
%exclude /usr/share/openvswitch/python/ovs/db/schema.py
%exclude /usr/share/openvswitch/python/ovs/db/types.py
%exclude /usr/share/openvswitch/python/ovs/dirs.py
%exclude /usr/share/openvswitch/python/ovs/fatal_signal.py
%exclude /usr/share/openvswitch/python/ovs/fcntl_win.py
%exclude /usr/share/openvswitch/python/ovs/json.py
%exclude /usr/share/openvswitch/python/ovs/jsonrpc.py
%exclude /usr/share/openvswitch/python/ovs/ovsuuid.py
%exclude /usr/share/openvswitch/python/ovs/poller.py
%exclude /usr/share/openvswitch/python/ovs/process.py
%exclude /usr/share/openvswitch/python/ovs/reconnect.py
%exclude /usr/share/openvswitch/python/ovs/socket_util.py
%exclude /usr/share/openvswitch/python/ovs/stream.py
%exclude /usr/share/openvswitch/python/ovs/timeval.py
%exclude /usr/share/openvswitch/python/ovs/unixctl/__init__.py
%exclude /usr/share/openvswitch/python/ovs/unixctl/client.py
%exclude /usr/share/openvswitch/python/ovs/unixctl/server.py
%exclude /usr/share/openvswitch/python/ovs/util.py
%exclude /usr/share/openvswitch/python/ovs/version.py
%exclude /usr/share/openvswitch/python/ovs/vlog.py
%exclude /usr/share/openvswitch/python/ovs/winutils.py
%exclude /usr/share/openvswitch/python/ovstest/__init__.py
%exclude /usr/share/openvswitch/python/ovstest/args.py
%exclude /usr/share/openvswitch/python/ovstest/rpcserver.py
%exclude /usr/share/openvswitch/python/ovstest/tcp.py
%exclude /usr/share/openvswitch/python/ovstest/tests.py
%exclude /usr/share/openvswitch/python/ovstest/udp.py
%exclude /usr/share/openvswitch/python/ovstest/util.py
%exclude /usr/share/openvswitch/python/ovstest/vswitch.py
%exclude /usr/share/openvswitch/scripts/ovs-check-dead-ifs
%exclude /usr/share/openvswitch/scripts/ovs-vtep
/usr/share/openvswitch/bugtool-plugins/kernel-info/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/network-status/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/network-status/ovn.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration.xml
/usr/share/openvswitch/bugtool-plugins/system-configuration/openvswitch.xml
/usr/share/openvswitch/bugtool-plugins/system-logs/openvswitch.xml
/usr/share/openvswitch/ovn-nb.ovsschema
/usr/share/openvswitch/ovn-sb.ovsschema
/usr/share/openvswitch/scripts/ovn-bugtool-nbctl-show
/usr/share/openvswitch/scripts/ovn-bugtool-sbctl-lflow-list
/usr/share/openvswitch/scripts/ovn-bugtool-sbctl-show
/usr/share/openvswitch/scripts/ovn-ctl
/usr/share/openvswitch/scripts/ovndb-servers.ocf
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
/usr/share/openvswitch/scripts/ovs-ctl
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
/usr/include/openflow/openflow-1.6.h
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
/usr/include/openvswitch/nsh.h
/usr/include/openvswitch/ofp-actions.h
/usr/include/openvswitch/ofp-ed-props.h
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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openvswitch/*

%files extras
%defattr(-,root,root,-)
/usr/bin/ovn-detrace
/usr/bin/ovn-docker-overlay-driver
/usr/bin/ovn-docker-underlay-driver
/usr/bin/ovs-bugtool
/usr/bin/ovs-dpctl-top
/usr/bin/ovs-l3ping
/usr/bin/ovs-parse-backtrace
/usr/bin/ovs-pcap
/usr/bin/ovs-tcpdump
/usr/bin/ovs-tcpundump
/usr/bin/ovs-test
/usr/bin/ovs-vlan-test
/usr/share/openvswitch/python/ovs/__init__.py
/usr/share/openvswitch/python/ovs/daemon.py
/usr/share/openvswitch/python/ovs/db/__init__.py
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
/usr/share/openvswitch/scripts/ovs-vtep

%files license
%defattr(-,root,root,-)
/usr/share/doc/openvswitch/COPYING
/usr/share/doc/openvswitch/xenserver_LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/ovn-detrace.1
/usr/share/man/man1/ovs-pcap.1
/usr/share/man/man1/ovs-tcpundump.1
/usr/share/man/man1/ovsdb-client.1
/usr/share/man/man1/ovsdb-server.1
/usr/share/man/man1/ovsdb-tool.1
/usr/share/man/man5/ovn-nb.5
/usr/share/man/man5/ovn-sb.5
/usr/share/man/man5/ovs-vswitchd.conf.db.5
/usr/share/man/man5/vtep.5
/usr/share/man/man7/ovn-architecture.7
/usr/share/man/man7/ovs-fields.7
/usr/share/man/man8/ovn-controller-vtep.8
/usr/share/man/man8/ovn-controller.8
/usr/share/man/man8/ovn-ctl.8
/usr/share/man/man8/ovn-nbctl.8
/usr/share/man/man8/ovn-northd.8
/usr/share/man/man8/ovn-sbctl.8
/usr/share/man/man8/ovn-trace.8
/usr/share/man/man8/ovs-appctl.8
/usr/share/man/man8/ovs-bugtool.8
/usr/share/man/man8/ovs-ctl.8
/usr/share/man/man8/ovs-dpctl-top.8
/usr/share/man/man8/ovs-dpctl.8
/usr/share/man/man8/ovs-l3ping.8
/usr/share/man/man8/ovs-ofctl.8
/usr/share/man/man8/ovs-parse-backtrace.8
/usr/share/man/man8/ovs-pki.8
/usr/share/man/man8/ovs-tcpdump.8
/usr/share/man/man8/ovs-testcontroller.8
/usr/share/man/man8/ovs-vlan-bug-workaround.8
/usr/share/man/man8/ovs-vsctl.8
/usr/share/man/man8/ovs-vswitchd.8
/usr/share/man/man8/vtep-ctl.8
