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
from urllib import quote
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1406885499.352325
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/epgpop.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class epgpop(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(epgpop, self).__init__(*args, **KWs)
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
        
        if len(VFFSL(SL,"events",True)) == 0: # generated from line 3, col 1
            write(u'''<html xmlns="http://www.w3.org/1999/xhtml">
<html>
<head>
<title>No items found.</title>
</head>
<body style="background: #FFFFFF; scrollbar: auto;">
<img src="/images/not_found.jpg" title="No items found" border="0">
</body>
</html>
''')
        else: # generated from line 13, col 1
            write(u'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link type="text/css" href="/css/jquery-ui-1.8.18.custom.css" rel="stylesheet" />\t
<script type="text/javascript" src="/js/jquery-1.6.2.min.js"></script>
<script type="text/javascript" src="/js/jquery-ui-1.8.18.custom.min.js"></script>
<script type="text/javascript" src="/js/openwebif.js"></script>
<style>
table { font-size:12px; font-family: Verdana,Arial,sans-serif;}
tr {background-color: #F0F7FC;}
</style>

<title>Open Webif ''')
            _v = VFFSL(SL,"tstrings",True)['epg'] # u"$tstrings['epg']" on line 29, col 19
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['epg']")) # from line 29, col 19.
            write(u'''</title>
</head>
\t<body style="background: #1C478E; scrollbar: auto;">
\t\t
''')
            for event in VFFSL(SL,"events",True): # generated from line 33, col 1
                write(u'''\t\t<table style="font-size:12px;" width="100%" border="0" cellspacing="1" cellpadding="5">
\t\t\t<tr>
\t\t\t\t<td style="padding:0px" width="102px"><img width="100px" height="60px" src="''')
                _v = VFFSL(SL,"event.picon",True) # u'$event.picon' on line 36, col 81
                if _v is not None: write(_filter(_v, rawExpr=u'$event.picon')) # from line 36, col 81.
                write(u'''" title="" border="0"></td>
\t\t\t\t<td style="font-size:13px;color: #061C37;font-weight: bold;" width="30%">''')
                _v = VFFSL(SL,"event.sname",True) # u'$event.sname' on line 37, col 78
                if _v is not None: write(_filter(_v, rawExpr=u'$event.sname')) # from line 37, col 78.
                write(u'''<br />''')
                _v = VFFSL(SL,"event.date",True) # u'$event.date' on line 37, col 96
                if _v is not None: write(_filter(_v, rawExpr=u'$event.date')) # from line 37, col 96.
                write(u'''</td>
\t\t\t\t<td>''')
                _v = VFFSL(SL,"event.title",True) # u'$event.title' on line 38, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$event.title')) # from line 38, col 9.
                write(u'''</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<td>''')
                _v = VFFSL(SL,"event.begin",True) # u'$event.begin' on line 41, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$event.begin')) # from line 41, col 9.
                write(u'''</td>
\t\t\t\t<td>''')
                _v = VFFSL(SL,"event.duration",True) # u'$event.duration' on line 42, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$event.duration')) # from line 42, col 9.
                write(u''' min.</td>
\t\t\t\t<td>''')
                _v = VFFSL(SL,"event.shortdesc",True) # u'$event.shortdesc' on line 43, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$event.shortdesc')) # from line 43, col 9.
                write(u'''</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<td valign="top">''')
                _v = VFFSL(SL,"event.end",True) # u'$event.end' on line 46, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'$event.end')) # from line 46, col 22.
                write(u'''</td>
\t\t\t\t<td colspan="2" rowspan="2">''')
                _v = VFFSL(SL,"event.longdesc",True) # u'$event.longdesc' on line 47, col 33
                if _v is not None: write(_filter(_v, rawExpr=u'$event.longdesc')) # from line 47, col 33.
                write(u'''</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<td style="padding:0px">
''')
                sref = quote(VFFSL(SL,"event.sref",True), safe=' ~@#$&()*!+=:;,.?/\'')
                write(u'''\t\t\t\t\t<a href="#" onclick="addTimerEvent(\'''')
                _v = VFFSL(SL,"sref",True) # u'$sref' on line 52, col 42
                if _v is not None: write(_filter(_v, rawExpr=u'$sref')) # from line 52, col 42.
                write(u"""',""")
                _v = VFFSL(SL,"event.id",True) # u'$event.id' on line 52, col 49
                if _v is not None: write(_filter(_v, rawExpr=u'$event.id')) # from line 52, col 49.
                write(u''');return false;"><img src="/images/timer.png" title="''')
                _v = VFFSL(SL,"tstrings",True)['add_timer'] # u"$tstrings['add_timer']" on line 52, col 111
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['add_timer']")) # from line 52, col 111.
                write(u'''" border="0"></a>\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t<a target="_blank" href="http://www.imdb.com/find?s=all&amp;q=''')
                _v = VFFSL(SL,"quote",False)(VFFSL(SL,"event.title",True)) # u'$quote($event.title)' on line 53, col 68
                if _v is not None: write(_filter(_v, rawExpr=u'$quote($event.title)')) # from line 53, col 68.
                write(u'''"><img src="/images/imdb.png" title="''')
                _v = VFFSL(SL,"tstrings",True)['search_imdb'] # u"$tstrings['search_imdb']" on line 53, col 125
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['search_imdb']")) # from line 53, col 125.
                write(u'''" border="0"></a>
\t\t\t\t</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<td colspan="3"></td>
\t\t\t</tr>
\t\t</table>
''')
            write(u'''\t\t\t\t
\t</body>
</html>
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

    _mainCheetahMethod_for_epgpop= 'respond'

## END CLASS DEFINITION

if not hasattr(epgpop, '_initCheetahAttributes'):
    templateAPIClass = getattr(epgpop, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(epgpop)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=epgpop()).run()


