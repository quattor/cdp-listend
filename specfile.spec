Summary: @DESCR@
Name: @NAME@
Version: @VERSION@
Vendor: EDG / CERN
Release: @RELEASE@
License: http://www.eu-datagrid.org/license.html
Group: @GROUP@
Source: @TARFILE@
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-build
Packager: @AUTHOR@
Obsoletes: edg-cdp-listend

%description 
description

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) @QTTR_SBIN@/cdp-listend
%attr(755,root,root) @QTTR_INITD@/cdp-listend
@QTTR_ETC@/cdp-listend.conf 
@QTTR_MAN@/man@MANSECT@/@COMP@.@MANSECT@.gz
@QTTR_DOC@/README
@QTTR_DOC@/MAINTAINER
@QTTR_DOC@/LICENSE
@QTTR_DOC@/ChangeLog

%post
SOname=`uname`
if [ $SOname = "Linux" ] ; then
  if [ "$1" = "1" ] ; then  # first install
	/sbin/chkconfig --add cdp-listend
	/sbin/service cdp-listend start > /dev/null 2>&1 || :
  fi
  if [ "$1" = "2" ] ; then  # upgrade
	/sbin/service cdp-listend restart > /dev/null 2>&1 || :
  fi
fi
if [ $SOname = "SunOS" ] ; then
	#*** cdp-listend logs messages as daemon.(info|err|debug)
	GREP_ENTRY=`grep "daemon.info" /etc/syslog.conf|grep -v '^#.*'`
	if [ -z "$GREP_ENTRY" ] ; then
	    #** By default, /etc/syslog.conf (from SUNWcsr) has this entry (not commented)
	    # *.err;kern.debug;daemon.notice;daemon.info;daemon.debug;mail.crit       /var/adm/messages
	    #*** I checked that if we put the new daemon entries at 
	    # the beginning of the line, they doesn't work.
	    CORRECTED=`sed -e s/'daemon\.notice'/'daemon\.notice\;daemon\.info\;daemon\.debug'/  /etc/syslog.conf`
	    rm -f /etc/syslog.conf
	    echo "$CORRECTED" > /etc/syslog.conf
	    echo "#*** daemon.info and daemon.debug entries added by cdp-listend">> /etc/syslog.conf
	    /etc/init.d/syslog stop > /dev/null 2>&1
	    /etc/init.d/syslog start > /dev/null 2>&1
	fi
 	#*** We make the startup and shutdown links
	ln -s @QTTR_INITD@/cdp-listend /etc/rc2.d/K15cdp-listend
	ln -s @QTTR_INITD@/cdp-listend /etc/rc3.d/S51cdp-listend	
	#*** We start the daemon now except if we are installing a new machine
        PGREP_INST=`pgrep -lf wp4.install`
	if [ -z "$PGREP_INST" ] ; then
	    @QTTR_INITD@/cdp-listend start > /dev/null 2>&1 || :
	fi
fi	

%preun
SOname=`uname`
if [ $SOname = "Linux" ] ; then
  if [ "$1" = "0" ] ; then  # last deinstall
        /sbin/chkconfig --del cdp-listend
	/sbin/service cdp-listend stop > /dev/null 2>&1 || :
  fi
fi
if [ $SOname = "SunOS" ] ; then
	rm /etc/rc2.d/K15cdp-listend
	rm /etc/rc3.d/S51cdp-listend
	@QTTR_INITD@/cdp-listend stop > /dev/null 2>&1 || :
fi






