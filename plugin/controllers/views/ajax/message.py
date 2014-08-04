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
__CHEETAH_genTime__ = 1406885499.345858
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/message.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class message(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(message, self).__init__(*args, **KWs)
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
        
        write(u'''<div id="content_main" style="min-height: 500px;">
\t<div id="info">
\t\t<h3>''')
        _v = VFFSL(SL,"tstrings",True)['send_message'] # u"$tstrings['send_message']" on line 4, col 7
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['send_message']")) # from line 4, col 7.
        write(u'''</h3>
\t\t<hr />
\t\t\t<div class="sendMessageContainer">
\t\t\t\t<table style="width: 50%;" align="center">
\t\t\t\t\t<tbody>
\t\t\t\t\t<tr>
\t\t\t\t\t\t<td>''')
        _v = VFFSL(SL,"tstrings",True)['text'] # u"$tstrings['text']" on line 10, col 11
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['text']")) # from line 10, col 11.
        write(u'''</td>
\t\t\t\t\t\t<td><textarea rows="3" cols="30" id="messageText"></textarea></td>
\t\t\t\t\t</tr>
\t\t\t\t\t<tr>
\t\t\t\t\t\t<td>''')
        _v = VFFSL(SL,"tstrings",True)['timeout'] # u"$tstrings['timeout']" on line 14, col 11
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['timeout']")) # from line 14, col 11.
        write(u'''</td>
\t\t\t\t\t\t<td><input type="text" value="30" id="messageTimeout"></td>
\t\t\t\t\t</tr>
\t\t\t\t\t<tr>
\t\t\t\t\t\t<td>''')
        _v = VFFSL(SL,"tstrings",True)['type'] # u"$tstrings['type']" on line 18, col 11
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['type']")) # from line 18, col 11.
        write(u'''</td>
\t\t\t\t\t\t<td>
\t\t\t\t\t\t\t<select id="messageType">
\t\t\t\t\t\t\t\t<option value="2">''')
        _v = VFFSL(SL,"tstrings",True)['info'] # u"$tstrings['info']" on line 21, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['info']")) # from line 21, col 27.
        write(u'''</option>
\t\t\t\t\t\t\t\t<option value="1">''')
        _v = VFFSL(SL,"tstrings",True)['warning'] # u"$tstrings['warning']" on line 22, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['warning']")) # from line 22, col 27.
        write(u'''</option>
\t\t\t\t\t\t\t\t<option value="3">''')
        _v = VFFSL(SL,"tstrings",True)['error'] # u"$tstrings['error']" on line 23, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['error']")) # from line 23, col 27.
        write(u'''</option>
\t\t\t\t\t\t\t\t<option value="0">''')
        _v = VFFSL(SL,"tstrings",True)['yes_no'] # u"$tstrings['yes_no']" on line 24, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['yes_no']")) # from line 24, col 27.
        write(u'''</option>
\t\t\t\t\t\t\t</select>
\t\t\t\t\t\t</td>
\t\t\t\t\t</tr>
\t\t\t\t\t<tr>
\t\t\t\t\t\t<td colspan="2" style="text-align: center;">
\t\t\t\t\t\t\t<button onclick="sendMessage();">''')
        _v = VFFSL(SL,"tstrings",True)['send_message'] # u"$tstrings['send_message']" on line 30, col 41
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['send_message']")) # from line 30, col 41.
        write(u'''</button>
\t\t\t\t\t\t\t<div id=''')
        _v = VFFSL(SL,"tstrings",True)['messageSentResponse'] # u"$tstrings['messageSentResponse']" on line 31, col 16
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['messageSentResponse']")) # from line 31, col 16.
        write(u'''></div>
\t\t\t\t\t\t</td>
\t\t\t\t\t</tr>
\t\t\t\t</tbody>
\t\t\t\t</table>
\t\t\t</div>
\t</div>
</div>
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

    _mainCheetahMethod_for_message= 'respond'

## END CLASS DEFINITION

if not hasattr(message, '_initCheetahAttributes'):
    templateAPIClass = getattr(message, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(message)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=message()).run()


