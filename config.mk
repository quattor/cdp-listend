#
# configuration values for the component
#

COMP=cdp-listend

NAME=$(COMP)
DESCR=Configuration Distribution Protocol client deamon
VERSION=1.0.19
RELEASE=1

AUTHOR=Piotr Poznanski
MAINTAINER=Juan Antonio Lopez Perez <Juan.Lopez.Perez@cern.ch>,German Cancio Melia <German.Cancio.Melia@cern.ch>

CONFIGFILE=$(QTTR_ETC)/cdp-listend.conf

TESTVARS=


# By default use soket type 'unix', except for Solaris that is 'stream'
# Also, use a different lock file on solaris
SOCKET_TYPE='unix'
LOCKFILE=/var/lock/subsys/cdp-listend
ifeq ($(QTTR_OS), Solaris)
  SOCKET_TYPE='inet'
  LOCKFILE=$(QTTR_LOCKD)/cdp-listend
endif
  
DATE=01/03/11 01:19
