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
__CHEETAH_genTime__ = 1406885499.306317
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/bqe.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class bqe(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(bqe, self).__init__(*args, **KWs)
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
        
        _orig_filter_14154417 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''
<style>
\t.select { width: 100%; }
\t.sortable { list-style-type: none; margin: 0; padding: 0; width: 200px; }
\t.sortable li { margin: 0 1px 1px 2px; padding-left: 1.5em; font-size: .8em;  height:20px;}
\t.sortable li span { margin: 0 0 0 -1.5em; display: inline-block; }

\t #bql li .handle { display: inline-block;width: 2em;}
\t #bqs li .handle { display: inline-block;width: 2em;}

\t.selectable .ui-selecting { background: #FECA40; }
\t.selectable .ui-selected { background: #F39814; color: white; }
\t.selectable { list-style-type: none; margin: 0; padding: 0; width: 100%; }
\t.selectable li { margin: 1px; padding: 0.1em; font-size: 1em; height: 20px; }
</style>
<div id="content_main" style="min-height: 500px;">
<div id="info">
<h3>Bouquet Editor (BETA)</h3>
<div style="background-color: #EEE">
<div style="display: inline-block; width: 100%; zoom: 1;">

<div style="width:50%; height:50%; float:left">
<div style="padding:5px;">

<div id="toolbar-header">
<span id="toolbar"><span id="tb1">
<input type="radio" id="btn0" name="tb1" checked="checked" /><label for="btn0">TV</label>
<input type="radio" id="btn1" name="tb1"/><label for="btn1">Radio</label>
</span></span>
</div>

<div id="toolbar-header">
<span id="toolbar"><span id="tb2">
<input type="radio" id="btn2" name="tb2" /><label for="btn2">Satellites</label>
<input type="radio" id="btn3" name="tb2" checked="checked" /><label for="btn3">Provider</label>
<input type="radio" id="btn4" name="tb2" /><label for="btn4">All Services</label>
</span></span>
</div>
\t<div id="sel0" style="height: 200px;overflow-y:scroll;">
\t<ol id="provider" class="selectable" >
\t</ol>
\t</div>
\t<div style="margin:5px 0 5px 0;">
\t\t<button id=\'btnaddp\' onclick="addprovider(); return false;">Add Provider as new Bouquet</button>
\t</div>
\t<div>
\t<div style="margin:5px 0 5px 0;">
\tSearch :<input id="searchch" value="...">
\t</div>
\t</div>

\t<div id="sel1" style="height: 300px;overflow-y:scroll;">
\t<ol id="channels" class="selectable" >
\t</ol>
\t</div>
\t
\t<div style="margin:5px 0 5px 0;">
\t\t<button id=\'btnaddc\' onclick="addchannel(); return false;">Add channel(s) to Bouquet</button>
\t\t<button id=\'btnadda\' onclick="addalter(); return false;">Add channel(s) as alternate</button>
\t</div>

</div></div>

<div style="width:50%; height:50%; float:right">
<div style="padding:5px;">
<div id="toolbar-header">
<span id="toolbar"><span id="tb3">
<button id="btn5">Reload</button>
<button id="btn6">Backup</button>
<button id="btn7">Restore</button>
</span></span>
</div>
\t<div style="padding:5px;">
\t<div id="sel2" style="height: 280px;overflow-y:scroll;">
\t<ol id="bql" class="selectable" >
\t</ol>
\t</div>
\t<div style="margin:5px 0 5px 0;">
\t\t<button id=\'btnbadd\' onclick="addbq(); return false;">Add BQ</button>
\t\t<button id=\'btnbren\' onclick="renbq(); return false;">Ren BQ</button>
\t\t<button id=\'btnbdel\' onclick="delbq(); return false;">Del BQ</button>
\t</div>
\t
\t<div id="sel3" style="height: 300px;overflow-y:scroll;">
\t<ol id="bqs" class="selectable" >
\t</ol>
\t</div>
\t<div style="margin:5px 0 5px 0;">
\t\t<button id=\'btncdel\' onclick="delc(); return false;">Del channel(s)</button>
\t\t<button id=\'btnmadd\' onclick="addm(); return false;">Add marker</button>
\t\t<button id=\'btnmgren\' onclick="renmg(); return false;">Rename</button>
\t</div>
\t
\t</div>
</div>

</div>
</div>
<div id="errorbox" class="timerlist_row" style="color: red;">
\t<div class="ui-state-error ui-corner-all" style="padding: 0 .7em;"> 
\t<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span> 
\t\t<span id="error"></span>
\t\t<span id="success" style="color: green;"></span>
\t</div>
</div>

</div></div></div>

<script type="text/javascript" src="/js/bqe.js"></script>
<script type="text/javascript">
$(function() { InitPage();});
</script>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_14154417
        
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

    _mainCheetahMethod_for_bqe= 'respond'

## END CLASS DEFINITION

if not hasattr(bqe, '_initCheetahAttributes'):
    templateAPIClass = getattr(bqe, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(bqe)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=bqe()).run()

