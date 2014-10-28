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
__CHEETAH_genTime__ = 1406885499.258124
__CHEETAH_genTimestamp__ = 'Fri Aug  1 18:31:39 2014'
__CHEETAH_src__ = '/home/wslee2/models/5-wo/force1plus/openpli3.0/build-force1plus/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-1+git5+3c0c4fbdb28d7153bf2140459b553b3d5cdd4149-r0/git/plugin/controllers/views/ajax/about.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug  1 18:30:05 2014'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class about(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(about, self).__init__(*args, **KWs)
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
        
        write(u'''<!-- about -->
\t\t<div id="content_main">
\t\t\t<div id="info">
\t\t\t\t<h3>OpenWebif</h3>
\t\t\t\t<h2>''')
        _v = VFFSL(SL,"tstrings",True)['openwebif_header'] # u"$tstrings['openwebif_header']" on line 6, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['openwebif_header']")) # from line 6, col 9.
        write(u'''</h2>
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['version'] # u"$tstrings['version']" on line 7, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['version']")) # from line 7, col 9.
        write(u''': ''')
        _v = VFFSL(SL,"info.owiver",True) # u'$info.owiver' on line 7, col 31
        if _v is not None: write(_filter(_v, rawExpr=u'$info.owiver')) # from line 7, col 31.
        write(u'''</h1>
\t\t\t\t<h2>''')
        _v = VFFSL(SL,"tstrings",True)['site_source'] # u"$tstrings['site_source']" on line 8, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['site_source']")) # from line 8, col 9.
        write(u''': <a href=\'https://github.com/E2OpenPlugins/e2openplugin-OpenWebif\'>Github</a></h2>
\t\t\t\t<hr />\t\t\t
\t\t\t\t<img src="images/about.jpg" alt="about">
\t\t\t\t<hr />
\t\t\t\t<br/>
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['authors'] # u"$tstrings['authors']" on line 13, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['authors']")) # from line 13, col 9.
        write(u'''</h1>
\t\t\t\t<div class="info">
\t\t\t\t\tmeo aka bacicciosat<br/>\t
\t\t\t\t\tskaman<br/>
\t\t\t\t\thomey-GER<br/>
\t\t\t\t\tnobody9<br/>
\t\t\t\t\trincewind<br/>
\t\t\t\t\tjbleyel<br/>
\t\t\t\t\tschimmelreiter<br/>
\t\t\t\t\tplnick
\t\t\t\t</div>
\t\t\t\t<br/>
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['contributors'] # u"$tstrings['contributors']" on line 25, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['contributors']")) # from line 25, col 9.
        write(u'''</h1>
\t\t\t\t<div class="info">
\t\t\t\t\tArmy (Graphics)<br/>
\t\t\t\t\tMilo, Cimarast<br/>
\t\t\t\t\tHSA (''')
        _v = VFFSL(SL,"tstrings",True)['translation_spanish'] # u"$tstrings['translation_spanish']" on line 29, col 11
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['translation_spanish']")) # from line 29, col 11.
        write(u''')<br/>
\t\t\t\t</div>
\t\t\t\t<br/>
\t\t\t\t<hr />
\t\t\t\t<br/>\t
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['javalib'] # u"$tstrings['javalib']" on line 34, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['javalib']")) # from line 34, col 9.
        write(u'''</h1>
\t\t\t\t<div class="info">
\t\t\t\t\t<a href=\'http://jqueryui.com/\'>Jquery UI</a>
\t\t\t\t</div>
\t\t\t\t<br/>
\t\t\t\t<hr />
\t\t\t\t<br/>\t
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['template_engine'] # u"$tstrings['template_engine']" on line 41, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['template_engine']")) # from line 41, col 9.
        write(u'''</h1>
\t\t\t\t<div class="info">
\t\t\t\t\t<a href=\'http://www.cheetahtemplate.org/\'>Cheetah</a>
\t\t\t\t</div>
\t\t\t\t<br/>
\t\t\t\t<hr />
\t\t\t\t<br/>\t\t\t
\t\t\t\t<h1>''')
        _v = VFFSL(SL,"tstrings",True)['license'] # u"$tstrings['license']" on line 48, col 9
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['license']")) # from line 48, col 9.
        write(u'''</h1>
\t\t\t\t<pre class="info">
''')
        _v = VFFSL(SL,"tstrings",True)['license_text_01'] # u"$tstrings['license_text_01']" on line 50, col 1
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['license_text_01']")) # from line 50, col 1.
        write(u'''
''')
        _v = VFFSL(SL,"tstrings",True)['license_text_02'] # u"$tstrings['license_text_02']" on line 51, col 1
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['license_text_02']")) # from line 51, col 1.
        write(u'''
''')
        _v = VFFSL(SL,"tstrings",True)['license_text_03'] # u"$tstrings['license_text_03']" on line 52, col 1
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['license_text_03']")) # from line 52, col 1.
        write(u'''
''')
        _v = VFFSL(SL,"tstrings",True)['license_text_04'] # u"$tstrings['license_text_04']" on line 53, col 1
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['license_text_04']")) # from line 53, col 1.
        write(u'''
\t\t\t\t</pre>

\t\t\t</div>
\t\t</div>\t
<!-- /about -->
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

    _mainCheetahMethod_for_about= 'respond'

## END CLASS DEFINITION

if not hasattr(about, '_initCheetahAttributes'):
    templateAPIClass = getattr(about, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(about)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=about()).run()

