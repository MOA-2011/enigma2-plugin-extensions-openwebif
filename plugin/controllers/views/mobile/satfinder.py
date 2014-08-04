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
__CHEETAH_genTime__ = 1406885498.414901
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:38 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/mobile/satfinder.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class satfinder(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(satfinder, self).__init__(*args, **KWs)
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
 <body>\r
\t<div data-role="page" id="mainPage">\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">''')
        _v = VFFSL(SL,"tstrings",True)['back'] # u"$tstrings['back']" on line 16, col 49
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['back']")) # from line 16, col 49.
        write(u'''</div>\r
\t\t\t<h1><a style="color:#FFF;text-decoration:none;" href=\'/mobile\'>OpenWebif</a></h1>
\t\t</div>\r
\r
\t\t<div id="contentContainer">\r
\t\t\t<div id="mainContent" class="ui-corner-all">\r
\t\t\t\r
\t\t\t<table width="100%" border="0" cellspacing="1" cellpadding="5">\r
\t\t\t\t<tr>\r
\t\t\t\t\t<td style="width: 30px;">''')
        _v = VFFSL(SL,"tstrings",True)['snr'] # u"$tstrings['snr']" on line 25, col 31
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['snr']")) # from line 25, col 31.
        write(u''':</td>\r
\t\t\t\t\t<td>\r
\t\t\t\t\t\t<div class="ui-btn-down-d ui-btn-corner-all" style="height: 22px;">\r
\t\t\t\t\t\t\t<div name="snrslider" id="snrslider" class="ui-btn-up-b ui-btn-corner-all ui-shadow" style="width: 0%; height: 20px; text-align: center;">0</div>\r
\t\t\t\t\t\t</div>\r
\t\t\t\t\t</td>\r
\t\t\t\t</tr>\r
\t\t\t\t<tr>\r
\t\t\t\t\t<td style="width: 30px;">''')
        _v = VFFSL(SL,"tstrings",True)['agc'] # u"$tstrings['agc']" on line 33, col 31
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['agc']")) # from line 33, col 31.
        write(u''':</td>\r
\t\t\t\t\t<td>\r
\t\t\t\t\t\t<div class="ui-btn-down-d ui-btn-corner-all" style="height: 22px;">\r
\t\t\t\t\t\t\t<div name="agcslider" id="agcslider" class="ui-btn-up-b ui-btn-corner-all ui-shadow" style="width: 0%; height: 20px; text-align: center;">0</div>\r
\t\t\t\t\t\t</div>\r
\t\t\t\t\t</td>\r
\t\t\t\t</tr>\r
\t\t\t\t<tr>\r
\t\t\t\t\t<td style="width: 30px;">''')
        _v = VFFSL(SL,"tstrings",True)['ber'] # u"$tstrings['ber']" on line 41, col 31
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['ber']")) # from line 41, col 31.
        write(u''':</td>\r
\t\t\t\t\t<td>\r
\t\t\t\t\t\t<div class="ui-btn-down-d ui-btn-corner-all" style="height: 22px;">\r
\t\t\t\t\t\t\t<div name="berslider" id="berslider" style="width: 100%; height: 20px; text-align: center;">0</div>\r
\t\t\t\t\t\t</div>\r
\t\t\t\t\t</td>\r
\t\t\t\t</tr>\r
\t\t\t</table>\r
\r
\t\t\t</div>\r
\t\t</div>\r
\t\t\r
\t\t<div id="footer">\r
\t\t\t<p>OpenWebif Mobile</p>\r
\t\t\t<a onclick="document.location.href=\'/index?mode=fullpage\';return false;" href="#">''')
        _v = VFFSL(SL,"tstrings",True)['show_full_openwebif'] # u"$tstrings['show_full_openwebif']" on line 55, col 86
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_full_openwebif']")) # from line 55, col 86.
        write(u'''</a>\r
\t\t</div>\r
\r
\t<script>\r
\tfunction getFrontendStatus() {\r
\t\tjQuery.getJSON(\'/api/signal\')\r
\t\t.success(function(statusinfo) {\r
\t\t\t jQuery(\'#snrslider\').css(\'width\', statusinfo[\'snr\']+\'%\').html(statusinfo[\'snr\']+\'%\');\r
\t\t\t jQuery(\'#agcslider\').css(\'width\', statusinfo[\'agc\']+\'%\').html(statusinfo[\'agc\']+\'%\');\r
\t\t\t jQuery(\'#berslider\').css(\'width\', \'100%\').html(statusinfo[\'ber\']);\r
\t\t\t setTimeout("getFrontendStatus()", 5000);\r
\t\t});\r
\t\treturn true;\r
\t}\r
\t\r
\tgetFrontendStatus();\r
\t</script>\r
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

    _mainCheetahMethod_for_satfinder= 'respond'

## END CLASS DEFINITION

if not hasattr(satfinder, '_initCheetahAttributes'):
    templateAPIClass = getattr(satfinder, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(satfinder)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=satfinder()).run()


