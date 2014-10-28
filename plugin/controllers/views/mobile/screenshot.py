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
__CHEETAH_genTime__ = 1406885498.431111
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:38 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/mobile/screenshot.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class screenshot(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(screenshot, self).__init__(*args, **KWs)
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
\t<div data-role="page">\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">''')
        _v = VFFSL(SL,"tstrings",True)['back'] # u"$tstrings['back']" on line 16, col 49
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['back']")) # from line 16, col 49.
        write(u'''</div>\r
\t\t\t<h1><a style="color:#FFF;text-decoration:none;" href=\'/mobile\'>OpenWebif</a></h1>
\t\t</div>\r
\t\t\r
\t\t<div>\r
\t\t\t<fieldset data-type="horizontal" data-role="controlgroup" style="width: 275px; margin: auto; margin-top: 15px;">\r
\t\t\t   <div onClick="jQuery(\'#screenshot\').attr(\'src\',\'/grab?r=275&mode=all&timestamp=\' + new Date().getTime()); return false;"><input type="radio" id="radio-view-a" name="radio-view"><label for="radio-view-a" data-theme="c">''')
        _v = VFFSL(SL,"tstrings",True)['all'] # u"$tstrings['all']" on line 22, col 225
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['all']")) # from line 22, col 225.
        write(u'''</label></div>\r
\t\t\t   <div onClick="jQuery(\'#screenshot\').attr(\'src\',\'/grab?r=275&mode=video&timestamp=\' + new Date().getTime()); return false;"><input type="radio" id="radio-view-b" name="radio-view"><label for="radio-view-b" data-theme="c">''')
        _v = VFFSL(SL,"tstrings",True)['video'] # u"$tstrings['video']" on line 23, col 227
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['video']")) # from line 23, col 227.
        write(u'''</label></div>\r
\t\t\t   <div onClick="jQuery(\'#screenshot\').attr(\'src\',\'/grab?r=275&mode=osd&timestamp=\' + new Date().getTime()); return false;"><input type="radio" id="radio-view-c" name="radio-view"><label for="radio-view-c" data-theme="c">''')
        _v = VFFSL(SL,"tstrings",True)['osd'] # u"$tstrings['osd']" on line 24, col 225
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['osd']")) # from line 24, col 225.
        write(u'''</label></div>\r
\t\t\t</fieldset>\r
\t\t\t\r
\t\t\t<div id="mainContent">\r
\t\t\t\t<img id="screenshot" src="/grab?r=275&mode=all" width="275" height="154" alt="''')
        _v = VFFSL(SL,"tstrings",True)['screenshot'] # u"$tstrings['screenshot']" on line 28, col 83
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['screenshot']")) # from line 28, col 83.
        write(u'''">\r
\t\t\t</div>\r
\t\t\t\r
\t\t\t<a href="#" onClick="location.reload(true)" data-role="button">''')
        _v = VFFSL(SL,"tstrings",True)['refresh'] # u"$tstrings['refresh']" on line 31, col 67
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['refresh']")) # from line 31, col 67.
        write(u'''</a>\r
\t\t\t\r
\t\t\t<div id="footer">\r
\t\t\t\t<p>OpenWebif Mobile</p>\r
\t\t\t\t<a onclick="document.location.href=\'/index?mode=fullpage\';return false;" href="#">''')
        _v = VFFSL(SL,"tstrings",True)['show_full_openwebif'] # u"$tstrings['show_full_openwebif']" on line 35, col 87
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_full_openwebif']")) # from line 35, col 87.
        write(u'''</a>\r
\t\t\t</div>\r
\t\t</div>\r
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

    _mainCheetahMethod_for_screenshot= 'respond'

## END CLASS DEFINITION

if not hasattr(screenshot, '_initCheetahAttributes'):
    templateAPIClass = getattr(screenshot, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(screenshot)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=screenshot()).run()

