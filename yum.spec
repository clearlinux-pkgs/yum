#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yum
Version  : 3.4.3
Release  : 40
URL      : http://yum.baseurl.org/download/3.4/yum-3.4.3.tar.gz
Source0  : http://yum.baseurl.org/download/3.4/yum-3.4.3.tar.gz
Summary  : RPM installer/updater
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: yum-bin
Requires: yum-data
Requires: yum-license
Requires: yum-locales
Requires: yum-man
Requires: yum-python
Requires: pycurl-legacypython
Requires: pyliblzma-legacypython
Requires: python-rpm-legacypython
Requires: yum-legacypython
BuildRequires : gettext-bin
BuildRequires : intltool
BuildRequires : python-dev
Patch1: cve-2014-0022.nopatch
Patch2: 0001-Improve-yum-performance-in-Clear.patch
Patch3: 0002-No-lock.patch
Patch4: 0003-Force-usr-bin-python2.patch

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded 
automatically, prompting the user for permission as necessary.

%package bin
Summary: bin components for the yum package.
Group: Binaries
Requires: yum-data
Requires: yum-license
Requires: yum-man

%description bin
bin components for the yum package.


%package data
Summary: data components for the yum package.
Group: Data

%description data
data components for the yum package.


%package legacypython
Summary: legacypython components for the yum package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the yum package.


%package license
Summary: license components for the yum package.
Group: Default

%description license
license components for the yum package.


%package locales
Summary: locales components for the yum package.
Group: Default

%description locales
locales components for the yum package.


%package man
Summary: man components for the yum package.
Group: Default

%description man
man components for the yum package.


%package python
Summary: python components for the yum package.
Group: Default

%description python
python components for the yum package.


%prep
%setup -q -n yum-3.4.3
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529093448
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags} DESTDIR=%{buildroot}

%install
export SOURCE_DATE_EPOCH=1529093448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/yum
cp COPYING %{buildroot}/usr/share/doc/yum/COPYING
%make_install
%find_lang yum
## make_install_append content
rm -rf %{buildroot}%{_sysconfdir}/rc.d
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf %{buildroot}%{_datadir}/dbus-1/system.d
rm -rf %{buildroot}%{_sysconfdir}/dbus-1/
rm -rf %{buildroot}%{_sysconfdir}/cron.daily
rm -rf %{buildroot}%{_sysconfdir}/sysconfig
rm -rf %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/yum.bash %{buildroot}%{_datadir}/bash-completion/completions/yum
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d
rm -rf %{buildroot}%{_sysconfdir}/yum
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yum
/usr/bin/yum-updatesd

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/yum
/usr/share/dbus-1/system.d/yum-updatesd.conf
/usr/share/yum-cli/callback.py
/usr/share/yum-cli/callback.pyc
/usr/share/yum-cli/cli.py
/usr/share/yum-cli/cli.pyc
/usr/share/yum-cli/output.py
/usr/share/yum-cli/output.pyc
/usr/share/yum-cli/shell.py
/usr/share/yum-cli/shell.pyc
/usr/share/yum-cli/utils.py
/usr/share/yum-cli/utils.pyc
/usr/share/yum-cli/yumcommands.py
/usr/share/yum-cli/yumcommands.pyc
/usr/share/yum-cli/yummain.py
/usr/share/yum-cli/yummain.pyc
/usr/share/yum-cli/yumupd.py
/usr/share/yum-cli/yumupd.pyc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/yum/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man5/yum-updatesd.conf.5
/usr/share/man/man5/yum.conf.5
/usr/share/man/man8/yum-shell.8
/usr/share/man/man8/yum-updatesd.8
/usr/share/man/man8/yum.8

%files python
%defattr(-,root,root,-)

%files locales -f yum.lang
%defattr(-,root,root,-)

