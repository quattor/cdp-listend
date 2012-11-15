# CDP-LISTEND

[![Build Status](https://jenkins1.ugent.be/view/Quattor/job/cdp-listend/badge/icon)](https://jenkins1.ugent.be/view/Quattor/job/cdp-listend/)

This is the client configuration system for [Quattor](http://quattor.org)

It consists of:
 - the cdp-listend daemon

This daemon supports the CDP notifications. Upon receiving the
notification it runs the ccm-fetch or nch applications.  It should be
installed on the machine where any of this software is installed so
that it is capable to react to the notifications sent.

Licensing information can be found in the LICENSE file.
