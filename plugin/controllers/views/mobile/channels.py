#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1406885498.38012
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:38 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/mobile/channels.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class channels(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(channels, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<html>\r
 <head>\r
\t<title>OpenWebif</title>\r
\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r
\t<meta name="viewport" content="user-scalable=no, width=device-width"/>\r
\t<meta name="apple-mobile-web-app-capable" content="yes" />\r
\t<link rel="stylesheet" type="text/css" href="/css/jquery.mobile-1.0.min.css" media="screen"/>\r
\t<link rel="stylesheet" type="text/css" href="/css/iphone.css" media="screen"/>\r
\t<script src="/js/jquery-1.6.2.min.js"></script>\r
\t<script src="/js/jquery.mobile-1.0.min.js"></script>\r
 </head>\r
 <body> \r
\t<div data-role="page">\r
\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">''')
        _v = VFFSL(SL,"tstrings",True)['back'] # u"$tstrings['back']" on line 17, col 49
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['back']")) # from line 17, col 49.
        write(u'''</div>\r
\t\t\t<h1><a style="color:#FFF;text-decoration:none;" href=\'/mobile\'>OpenWebif</a></h1>
\t\t</div>\r
\r
\t\t<div id="contentContainer">\r
\t\t\t<ul data-role="listview" data-inset="true" data-theme="d">\r
\t\t\t\t<li data-role="list-divider" role="heading" data-theme="b">''')
        _v = VFFSL(SL,"tstrings",True)['channels'] # u"$tstrings['channels']" on line 23, col 64
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['channels']")) # from line 23, col 64.
        write(u'''</li>\r
''')
        for channel in VFFSL(SL,"channels",True): # generated from line 24, col 5
            write(u'''\t\t\t\t<li>\r
\t\t\t\t<a href="/mobile/channelinfo?sref=''')
            _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 26, col 39
            if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 26, col 39.
            write(u'''" style="padding: 3px;">\r
\t\t\t\t<span class="ui-li-heading" style="margin-top: 0px; margin-bottom: 3px;">''')
            _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 27, col 78
            if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 27, col 78.
            write(u'''</span>\r
''')
            if VFN(VFFSL(SL,"channel",True),"has_key",False)('now_title'): # generated from line 28, col 5
                write(u'''\t\t\t\t<span class="ui-li-desc" style="margin-bottom: 0px;">''')
                _v = VFFSL(SL,"channel.now_title",True) # u'$channel.now_title' on line 29, col 58
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_title')) # from line 29, col 58.
                write(u'''</span>\r
''')
            write(u'''\t\t\t\t</a>\r
\t\t\t\t</li>\r
''')
        write(u'''\t\t\t</ul>\r
\t\t</div>\r
\r
\t\t<div id="footer">\r
\t\t\t<p>OpenWebif Mobile</p>\r
\t\t\t<a onclick="document.location.href=\'/index?mode=fullpage\';return false;" href="#">''')
        _v = VFFSL(SL,"tstrings",True)['show_full_openwebif'] # u"$tstrings['show_full_openwebif']" on line 39, col 86
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_full_openwebif']")) # from line 39, col 86.
        write(u'''</a>\r
\t\t</div>\r
\t\t\r
\t</div>\r
 </body>\r
</html>\r
      ''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_channels= 'respond'

## END CLASS DEFINITION

if not hasattr(channels, '_initCheetahAttributes'):
    templateAPIClass = getattr(channels, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(channels)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=channels()).run()


