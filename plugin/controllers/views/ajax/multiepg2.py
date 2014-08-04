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
from json import dumps
from Plugins.Extensions.OpenWebif.controllers.views.ajax.renderevtblock import renderEvtBlock

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1406885499.272806
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/multiepg2.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class multiepg2(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(multiepg2, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def channelsInBouquet(self, **KWS):



        ## CHEETAH: generated from #block channelsInBouquet at line 72, col 1.
        trans = KWS.get("trans")
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
        
        write(u'''<thead>
<tr>
''')
        for sname, eventlist in VFN(VFFSL(SL,"events",True),"iteritems",False)(): # generated from line 75, col 2
            write(u'''\t<th class="border"><div class="service"><img src="''')
            _v = VFFSL(SL,"picons",True)[VFFSL(SL,"sname",True)] # u'$(picons[$sname])' on line 76, col 52
            if _v is not None: write(_filter(_v, rawExpr=u'$(picons[$sname])')) # from line 76, col 52.
            write(u'''" /> ''')
            _v = VFFSL(SL,"sname",True) # u'$sname' on line 76, col 74
            if _v is not None: write(_filter(_v, rawExpr=u'$sname')) # from line 76, col 74.
            write(u'''</div></th>
''')
        write(u'''</tr>
</thead>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

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
        
        write(u'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="/images/favicon.png">
<link rel="stylesheet" type="text/css" href="/css/style.css" />
<link type="text/css" href="/css/jquery-ui-1.8.18.custom.css" rel="stylesheet" />\t
<script type="text/javascript" src="/js/jquery-1.6.2.min.js"></script>
<script type="text/javascript" src="/js/jquery-ui-1.8.18.custom.min.js"></script>
<script type="text/javascript" src="/js/openwebif.js"></script>
<script type="text/javascript" src="/js/jquery.fixedheadertable.min.js"></script>
<script type="text/javascript">initJsTranslation(''')
        _v = VFFSL(SL,"dumps",False)(VFFSL(SL,"tstrings",True)) # u'$dumps($tstrings)' on line 17, col 50
        if _v is not None: write(_filter(_v, rawExpr=u'$dumps($tstrings)')) # from line 17, col 50.
        write(u''')</script>

<title>Open Webif ''')
        _v = VFFSL(SL,"tstrings",True)['multi_epg'] # u"$tstrings['multi_epg']" on line 19, col 19
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['multi_epg']")) # from line 19, col 19.
        write(u'''</title>
</head>

<body>

<style>
body {background-image: none;background-color: #FFF; }
#tvcontent {padding:0px;}
table { font-family: Verdana; font-size: 11px; }
tr { vertical-align: top }
.service { font-weight: bold; font-size: 12px; color:#fff; background-color: #1c47ae; line-height:30px; padding: 3px; white-space: nowrap; overflow: hidden; width: 184px}
.service img { width:50px; height:30px; float:left; margin-right:10px; }
.title { font-weight: bold; color: #061c37; }
.desc { font-size: 10px; color: #176093; }
.even { background-color: #dfeffc; }
.border { border-right: 1px solid #4297d7; }
.event { cursor: pointer; width: 190px; overflow:hidden; }
.bq { background-color: #1c478e; font-size: 11px; font-weight: bold; color: #fff; padding: 2px 4px; line-height: 18px; cursor: pointer; white-space: nowrap; }
.bq.selected { color: #A9D1FA; }
.plus { background-color: #dfeffc; font-size: 13px; font-weight: bold; color: #1c478e; padding: 2px 4px; line-height: 21px; cursor: pointer; white-space: nowrap; }
.plus.selected { color: #ea7409; }
.timer { color: #f00; font-weight: bold; font-size: 10px; }
.timer.disabled { color: #f80; }
#eventdescription { width: 375px; height: auto; position: fixed; top: 205px; left: 350px; z-index: 1000; display: none; overflow: auto; }
html, body, #tvcontent { width:100%; height:100%;}
.fht-table,.fht-table thead,.fht-table tfoot,.fht-table tbody,.fht-table tr,.fht-table th,.fht-table td{font-size:100%;font:inherit;vertical-align:top;margin:0;padding:0}
.fht-table{border-collapse:collapse;border-spacing:0}
.fht-table-wrapper,.fht-table-wrapper .fht-thead,.fht-table-wrapper .fht-tfoot,.fht-table-wrapper .fht-fixed-column .fht-tbody,.fht-table-wrapper .fht-fixed-body .fht-tbody,.fht-table-wrapper .fht-tbody{overflow:hidden;position:relative}
.fht-table-wrapper .fht-fixed-body .fht-tbody,.fht-table-wrapper .fht-tbody{overflow:auto}
.fht-table-wrapper .fht-table .fht-cell{overflow:hidden;height:1px}
.fht-table-wrapper .fht-fixed-column,.fht-table-wrapper .fht-fixed-body{top:0;left:0;position:absolute}
.fht-table-wrapper .fht-fixed-column{z-index:1}
}
</style>
<div id="tvcontent">
<table style="margin:0">
<tr>
''')
        for slot in range(0,7): # generated from line 56, col 1
            write(u'''    <td class="plus ''')
            if VFFSL(SL,"slot",True)==VFFSL(SL,"day",True) : # generated from line 57, col 21
                _v =  'selected' 
                if _v is not None: write(_filter(_v))
            else:
                _v =  '' 
                if _v is not None: write(_filter(_v))
            write(u'''" js:day="''')
            _v = VFFSL(SL,"slot",True) # u'$(slot)' on line 57, col 72
            if _v is not None: write(_filter(_v, rawExpr=u'$(slot)')) # from line 57, col 72.
            write(u'''">''')
            _v = VFFSL(SL,"tstrings",True)[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))] # u'$tstrings[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))]' on line 57, col 81
            if _v is not None: write(_filter(_v, rawExpr=u'$tstrings[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))]')) # from line 57, col 81.
            write(u'''</td>
''')
        write(u'''</tr>
</table>

<table>
<tr>
''')
        for bq in VFFSL(SL,"bouquets",True): # generated from line 64, col 1
            write(u'''<td class="bq ''')
            if VFFSL(SL,"bq",True)[0]==VFFSL(SL,"bref",True) : # generated from line 65, col 15
                _v =  'selected' 
                if _v is not None: write(_filter(_v))
            else:
                _v =  '' 
                if _v is not None: write(_filter(_v))
            write(u'''" js:ref="''')
            _v = VFFSL(SL,"quote",False)(VFFSL(SL,"bq",True)[0]) # u'$quote($bq[0])' on line 65, col 68
            if _v is not None: write(_filter(_v, rawExpr=u'$quote($bq[0])')) # from line 65, col 68.
            write(u'''">''')
            _v = VFFSL(SL,"bq",True)[1] # u'$bq[1]' on line 65, col 84
            if _v is not None: write(_filter(_v, rawExpr=u'$bq[1]')) # from line 65, col 84.
            write(u'''</td>
''')
        write(u'''</tr>
</table>

''')
        renderEventBlock = VFFSL(SL,"renderEvtBlock",False)()
        write(u'''<table cellpadding="0" cellspacing="0" id="TBL1">
''')
        self.channelsInBouquet(trans=trans)
        write(u'''<tbody>
''')
        hasEvents = False
        for slot in range(0,12): # generated from line 83, col 2
            write(u'''<tr class="''')
            _v = VFFSL(SL,"slot",True)%2 and 'odd' or 'even' # u"$(slot%2 and 'odd' or 'even')" on line 84, col 12
            if _v is not None: write(_filter(_v, rawExpr=u"$(slot%2 and 'odd' or 'even')")) # from line 84, col 12.
            write(u'''">
''')
            for sname, eventlist in VFN(VFFSL(SL,"events",True),"iteritems",False)(): # generated from line 85, col 2
                write(u'''<td class="border">
''')
                for event in VFFSL(SL,"eventlist",True)[VFFSL(SL,"slot",True)]: # generated from line 87, col 2
                    write(u'''\t\t''')
                    _v = VFN(VFFSL(SL,"renderEventBlock",True),"render",False)(VFFSL(SL,"event",True)) # u'$renderEventBlock.render($event)' on line 88, col 3
                    if _v is not None: write(_filter(_v, rawExpr=u'$renderEventBlock.render($event)')) # from line 88, col 3.
                    write(u'''
''')
                    hasEvents = True
                write(u'''</td>
''')
            write(u'''</tr>
''')
        write(u'''</tbody>
</table>
</div>
<div id="eventdescription"></div>
''')
        if VFFSL(SL,"reloadtimer",True)==1: # generated from line 99, col 1
            write(u'''<div id="editTimerForm" title="''')
            _v = VFFSL(SL,"tstrings",True)['edit_timer'] # u"$tstrings['edit_timer']" on line 100, col 32
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['edit_timer']")) # from line 100, col 32.
            write(u'''"></div>
''')
        write(u'''
<script>
var picons = ''')
        _v = VFFSL(SL,"dumps",False)(VFFSL(SL,"picons",True)) # u'$dumps($picons)' on line 104, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$dumps($picons)')) # from line 104, col 14.
        write(u''';
var reloadTimers = false;
$(".bq").click(function() {
    var id = $(this).attr("js:ref");
    $("#tvcontent").html(loadspinner).load(\'/ajax/multiepg2?reloadtimer=0&bref=\'+id);
});
$(".event").click(function() {
    var id = $(this).attr("js:id");
    var ref = $(this).attr("js:ref");
    $("#eventdescription").load(\'/ajax/event?idev=\'+id+\'&sref=\'+escape(ref), function() { 
\t\t$("#eventdescription").show(200).draggable( { handle: ".handle" } );
    });
});
$(".plus").click(function() {
\tvar day = $(this).attr("js:day");
\t$("#tvcontent").html(loadspinner).load(\'/ajax/multiepg2?reloadtimer=0&bref=''')
        _v = VFFSL(SL,"quote",False)(VFFSL(SL,"bref",True)) # u'${quote($bref)}' on line 119, col 78
        if _v is not None: write(_filter(_v, rawExpr=u'${quote($bref)}')) # from line 119, col 78.
        write(u"""&day='+day);
});
$('#editTimerForm').load('/ajax/edittimer');

$('#TBL1').fixedHeaderTable({ 
\tfooter: true,
\tcloneHeadToFoot: true,
\taltClass: 'odd',
\tautoShow: true
});

</script>
</body>
</html>
""")
        
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

    _mainCheetahMethod_for_multiepg2= 'respond'

## END CLASS DEFINITION

if not hasattr(multiepg2, '_initCheetahAttributes'):
    templateAPIClass = getattr(multiepg2, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(multiepg2)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=multiepg2()).run()


