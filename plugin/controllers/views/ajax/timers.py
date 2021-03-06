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
__CHEETAH_genTime__ = 1406885499.198806
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/timers.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class timers(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(timers, self).__init__(*args, **KWs)
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
        
        _orig_filter_74880465 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<div id="content_main" style="min-height: 500px;">
\t<div id="info">
\t\t<h3>''')
        _v = VFFSL(SL,"tstrings",True)['timer_list'] # u"$tstrings['timer_list']" on line 6, col 7
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['timer_list']")) # from line 6, col 7.
        write(u'''</h3>

\t\t<div id="toolbar-header">
\t\t\t<span id="toolbar">
\t\t\t\t<span id="timerbuttons">
\t\t\t\t\t<button id="timerbutton0" onclick="addTimer(); return false">''')
        _v = VFFSL(SL,"tstrings",True)['add_timer'] # u"$tstrings['add_timer']" on line 11, col 67
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['add_timer']")) # from line 11, col 67.
        write(u'''</button>
\t\t\t\t\t<button id="timerbutton1" onclick="cleanupTimer(); return false">''')
        _v = VFFSL(SL,"tstrings",True)['cleanup_timer'] # u"$tstrings['cleanup_timer']" on line 12, col 71
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['cleanup_timer']")) # from line 12, col 71.
        write(u'''</button>
\t\t\t\t</span>
\t\t\t</span>
\t\t</div>

\t\t<div id="timers" style="height: 640px; overflow: auto;">
''')
        for timer in VFFSL(SL,"timers",True): # generated from line 18, col 3
            write(u'''\t\t\t<div class="moviecontainer_main" id="''')
            _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 19, col 41
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 19, col 41.
            write(u'''-''')
            _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 19, col 54
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 19, col 54.
            write(u'''">
\t\t\t\t<div class="moviecontainer_left">
\t\t\t\t\t<div style="padding: 3px;">
\t\t\t\t\t\t<div style="color: #176093; font-weight: bold;">
\t\t\t\t\t\t\t''')
            _v = VFFSL(SL,"timer.name",True) # u'$timer.name' on line 23, col 8
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.name')) # from line 23, col 8.
            write(u'''
\t\t\t\t\t\t</div>
\t\t\t\t\t\t''')
            _v = VFFSL(SL,"timer.realbegin",True) # u'$timer.realbegin' on line 25, col 7
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.realbegin')) # from line 25, col 7.
            write(u''' - ''')
            _v = VFFSL(SL,"timer.realend",True) # u'$timer.realend' on line 25, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.realend')) # from line 25, col 26.
            write(u'''
''')
            if VFFSL(SL,"timer.repeated",True) != 0: # generated from line 26, col 7
                write(u'''\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t''')
                _v = VFFSL(SL,"tstrings",True)['every_timer'] # u"$tstrings['every_timer']" on line 28, col 9
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['every_timer']")) # from line 28, col 9.
                write(u'''
''')
                flags = VFFSL(SL,"timer.repeated",True)
                timerDays = []
                for day in [VFFSL(SL,"tstrings",True)['monday'],VFFSL(SL,"tstrings",True)['tuesday'],VFFSL(SL,"tstrings",True)['wednesday'],VFFSL(SL,"tstrings",True)['thursday'],VFFSL(SL,"tstrings",True)['friday'],VFFSL(SL,"tstrings",True)['saturday'],VFFSL(SL,"tstrings",True)['sunday']]: # generated from line 31, col 8
                    if VFFSL(SL,"flags",True)&1: # generated from line 32, col 9
                        write(u'''\t\t\t\t\t\t\t\t\t''')
                        _v = VFN(VFFSL(SL,"timerDays",True),"append",False)(VFFSL(SL,"day",True)) # u'$timerDays.append($day)' on line 33, col 10
                        if _v is not None: write(_filter(_v, rawExpr=u'$timerDays.append($day)')) # from line 33, col 10.
                        write(u'''
''')
                    flags = VFFSL(SL,"flags",True) >> 1
                _v = ', '.join(VFFSL(SL,"timerDays",True))
                if _v is not None: write(_filter(_v))
                write(u'''\t\t\t\t\t\t\t</div>
''')
            write(u'''\t\t\t\t\t\t<div style="font-weight: bold;">
\t\t\t\t\t\t\t''')
            _v = VFFSL(SL,"timer.servicename",True) # u'$timer.servicename' on line 41, col 8
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.servicename')) # from line 41, col 8.
            write(u'''
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t\t<div style="padding: 3px;">
\t\t\t\t\t\t''')
            _v = VFFSL(SL,"timer.description",True) # u'$timer.description' on line 45, col 7
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.description')) # from line 45, col 7.
            write(u'''
\t\t\t\t\t</div>
\t\t\t\t\t<div style="padding: 3px;">
\t\t\t\t\t\t<span style="color: #7F8181; font-weight: bold;">
''')
            if VFFSL(SL,"timer.state",True) == 0: # generated from line 49, col 8
                write(u'''\t\t\t\t\t\t\t\t''')
                _v = VFFSL(SL,"tstrings",True)['waiting'] # u"$tstrings['waiting']" on line 50, col 9
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['waiting']")) # from line 50, col 9.
                write(u'''
''')
            elif VFFSL(SL,"timer.state",True) == 2: # generated from line 51, col 8
                write(u'''\t\t\t\t\t\t\t\t''')
                _v = VFFSL(SL,"tstrings",True)['running'] # u"$tstrings['running']" on line 52, col 9
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['running']")) # from line 52, col 9.
                write(u'''
''')
            elif VFFSL(SL,"timer.state",True) == 3: # generated from line 53, col 8
                write(u'''\t\t\t\t\t\t\t\t''')
                _v = VFFSL(SL,"tstrings",True)['finished'] # u"$tstrings['finished']" on line 54, col 9
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['finished']")) # from line 54, col 9.
                write(u'''
''')
            write(u'''\t\t\t\t\t\t</span>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t\t<div class="moviecontainer_right">
\t\t\t\t\t<div style="padding: 3px; text-align: right;">
''')
            sref = quote(VFFSL(SL,"timer.serviceref",True), safe=' ~@#$&()*!+=:;,.?/\'')
            write(u'''\t\t\t\t\t\t<a href=\'#\' onClick="editTimer(\'''')
            _v = VFFSL(SL,"sref",True) # u'$sref' on line 62, col 39
            if _v is not None: write(_filter(_v, rawExpr=u'$sref')) # from line 62, col 39.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 62, col 48
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 62, col 48.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 62, col 64
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 62, col 64.
            write(u'''\');"><img src="../images/ico_edit.png" title="''')
            _v = VFFSL(SL,"tstrings",True)['edit_timer'] # u"$tstrings['edit_timer']" on line 62, col 120
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['edit_timer']")) # from line 62, col 120.
            write(u'''" border="0"></a>
\t\t\t\t\t\t<a href=\'#\' onClick="deleteTimer(\'''')
            _v = VFFSL(SL,"sref",True) # u'$sref' on line 63, col 41
            if _v is not None: write(_filter(_v, rawExpr=u'$sref')) # from line 63, col 41.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 63, col 50
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 63, col 50.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 63, col 66
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 63, col 66.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.name",True) # u'$timer.name' on line 63, col 80
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.name')) # from line 63, col 80.
            write(u'''\');"><img src="../images/ico_delete.png" title="''')
            _v = VFFSL(SL,"tstrings",True)['delete_timer'] # u"$tstrings['delete_timer']" on line 63, col 139
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['delete_timer']")) # from line 63, col 139.
            write(u'''" border="0"></a>
\t\t\t\t\t\t<a href=\'#\' onClick="toggleTimerStatus(\'''')
            _v = VFFSL(SL,"sref",True) # u'$sref' on line 64, col 47
            if _v is not None: write(_filter(_v, rawExpr=u'$sref')) # from line 64, col 47.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 64, col 56
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 64, col 56.
            write(u"""', '""")
            _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 64, col 72
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 64, col 72.
            write(u'''\');">
''')
            if VFFSL(SL,"timer.disabled",True): # generated from line 65, col 7
                write(u'''\t\t\t\t\t\t<img id="img-''')
                _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 66, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 66, col 20.
                write(u'''-''')
                _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 66, col 33
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 66, col 33.
                write(u'''" src="../images/ico_disabled.png" title="''')
                _v = VFFSL(SL,"tstrings",True)['enable_timer'] # u"$tstrings['enable_timer']" on line 66, col 85
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['enable_timer']")) # from line 66, col 85.
                write(u'''" border="0">
''')
            else: # generated from line 67, col 7
                write(u'''\t\t\t\t\t\t<img id="img-''')
                _v = VFFSL(SL,"timer.begin",True) # u'$timer.begin' on line 68, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.begin')) # from line 68, col 20.
                write(u'''-''')
                _v = VFFSL(SL,"timer.end",True) # u'$timer.end' on line 68, col 33
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.end')) # from line 68, col 33.
                write(u'''" src="../images/ico_enabled.png" title="''')
                _v = VFFSL(SL,"tstrings",True)['disable_timer'] # u"$tstrings['disable_timer']" on line 68, col 84
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['disable_timer']")) # from line 68, col 84.
                write(u'''" border="0">
''')
            write(u'''\t\t\t\t\t\t</a>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t\t<div style="clear: both;"></div>
\t\t\t</div>
''')
        write(u'''\t\t</div>
\t</div>
</div>

<div id="editTimerForm"></div>

<script>
\t$(\'#timerbuttons\').buttonset();
    var reloadTimers = true;

    $(\'#editTimerForm\').load(\'/ajax/edittimer\');
</script>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_74880465
        
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

    _mainCheetahMethod_for_timers= 'respond'

## END CLASS DEFINITION

if not hasattr(timers, '_initCheetahAttributes'):
    templateAPIClass = getattr(timers, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(timers)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=timers()).run()


