# -*- coding: utf-8 -*-

##############################################################################
#                        2011 E2OpenPlugins                                  #
#                                                                            #
#  This file is open source software; you can redistribute it and/or modify  #
#     it under the terms of the GNU General Public License version 2 as      #
#               published by the Free Software Foundation.                   #
#                                                                            #
##############################################################################

from Tools.Directories import fileExists
from Components.config import config

from models.services import getCurrentService, getBouquets, getChannels, getSatellites, getProviders, getEventDesc, getChannelEpg, getSearchEpg, getCurrentFullInfo, getMultiEpg, getEvent
from models.info import getInfo, getPublicPath, getOpenWebifVer
from models.movies import getMovieList
from models.timers import getTimers
from models.config import getConfigs, getConfigsSections
from base import BaseController
from time import mktime, localtime
from models.locations import getLocations

class AjaxController(BaseController):
	def __init__(self, session, path = ""):
		BaseController.__init__(self, path)
		self.session = session

	def P_current(self, request):
		return getCurrentFullInfo(self.session)

	def P_bouquets(self, request):
		stype = "tv"
		if "stype" in request.args.keys():
			stype = request.args["stype"][0]
		bouq = getBouquets(stype)
		return { "bouquets": bouq['bouquets'], "stype": stype }

	def P_providers(self, request):
		stype = "tv"
		if "stype" in request.args.keys():
			stype = request.args["stype"][0]
		prov = getProviders(stype)
		return { "providers": prov['providers'], "stype": stype }

	def P_satellites(self, request):
		stype = "tv"
		if "stype" in request.args.keys():
			stype = request.args["stype"][0]
		sat = getSatellites(stype)
		return { "satellites": sat['satellites'], "stype": stype }

	def P_channels(self, request):
		stype = "tv"
		idbouquet = "ALL"
		if "stype" in request.args.keys():
			stype = request.args["stype"][0]
		if "id" in request.args.keys():
			idbouquet = request.args["id"][0]
		channels = getChannels(idbouquet, stype)
		info = getInfo()
		model = info["model"]
		chipset = info["chipset"] # for chipset 7356 transcoding
		channels['transcoding'] = False
		if model in ("solo2", "duo2", "solose", "vusolo2", "vuduo2", "vusolose", "xpeedlx3", "gbquad", "gbquadplus") or chipset in ("7356"):
			channels['transcoding'] = True
#		print "@@@@@@@@@@@@ chipset @@@@@@@@@@@@@@@", chipset 

		return channels

	def P_eventdescription(self, request):
		return getEventDesc(request.args["sref"][0], request.args["idev"][0])

	def P_event(self, request):
		event = getEvent(request.args["sref"][0], request.args["idev"][0])
		event['event']['recording_margin_before'] = config.recording.margin_before.value
		event['event']['recording_margin_after'] = config.recording.margin_after.value
		return event

	def P_about(self, request):
		info = {}
		info["owiver"] = getOpenWebifVer()
		return { "info": info }
	
	def P_boxinfo(self, request):
		info = getInfo()
		model = info["model"]
		if model in ("et9000", "et9200", "et9500"):
			model = "et9x00"
		elif model in ("et5000", "et6000", "et6x00"):
			model = "et5x00"
		elif model == "et4000":
			model = "et4x00"
		elif model == "xp1000":
			model = "xp1000"
		elif model.startswith("vu"):
			model = model.replace("vu", "")
		if fileExists("/etc/.brandtype"):
			ret_brand = open("/etc/.brandtype").read().strip().lower()
#			print "@@@@@ [model] @@@@@", model
			if ret_brand == "technomate":
				if model == "TM-NANO-3T COMBO":
					model = "tmnano3tcombo"
				elif model == "tmnano2super":
					model = "te_tmnano2super"
				elif model == "TM-NANO-SE":
					model = "tmnanose"
				elif model == "TM-NANO-SE Combo":
					model = "tmnanosecombo"
				elif model == "TM-NANO-SE M2":
					model = "tmnanosem2"
				elif model == "TM-NANO-SE Plus":
					model = "tmnanoseplus"
				elif model == "TM-NANO M3":
					model = "tmnanom3"
				else:
					model = info["model"]
			elif ret_brand == "edision":
				if model.endswith("OS1"):
					model = "optimussos1"
				elif model.endswith("OS2"):
					model = "optimussos2"
				elif model.endswith("OS1PLUS"):
					model = "ed_op1plus"
				elif model.endswith("OS2PLUS"):
					model = "ed_op2plus"
				elif model.endswith("OS3+"):
					model = "ed_force1plus"
				elif model.endswith("OS"):
					model = "optimussos"
				else:
					model = info["model"]
			elif ret_brand == "worldvision":
				if model == "Force1+":
					model = "wo_force1plus"
				elif model == "force1":
					model = "wo_force1"
				elif model == "force2solid":
					model = "wo_force2solid"
				elif model == "force2":
					model = "wo_force2solid"
				else:
					model = info["model"]
			elif ret_brand == "swiss":
				if model == "Force1+":
					model = "sw_force1plus"
				elif model == "force1":
					model = "sw_force1"
				else:
					model = info["model"]
			elif ret_brand == "xsarius":
				if model == "FUSION HD":
					model = "fusionhd"
				elif model == "FUSION HD SE":
					model = "fusionhdse"
				elif model == "PURE HD":
					model = "purehd"
				elif model == "SELF SAT":
					model = "selfsat"
				else:
					model = info["model"]
			elif ret_brand  == "iqon":
				if model == "Force1+":
					model = "iq_force1plus"
				elif model == "force1":
					model = "iq_force1"
				elif model == "force2":
					model = "iq_force2"
				elif model == "force2solid":
					model = "iq_force2"
				elif model == "force2plus":
					model = "iq_force2plus"
				elif model == "force2se":
					model = "iq_force2se"
				elif model == "force2nano":
					model = "iq_force2nano"
				elif model == "PURE HD":
					model = "purehd"
				elif model == "SELF SAT":
					model = "selfsat"
				elif model == "ios100hd":
					model = "iq_ios100"
				elif model == "ios200hd":
					model = "iq_ios200"
				elif model == "ios300hd":
					model = "iq_ios300"
				elif model == "ios300newhd":
					mdoel = "iq_ios300new"
				else:
					model = info["model"]
			else:
				model = info["model"]
		if fileExists(getPublicPath("/images/boxes/" + model + ".jpg")):
			info["boximage"] = model + ".jpg"
		else:
			info["boximage"] = "unknown.jpg"
		if model in ("tf7700hdpvr", "topf", "TF 7700 HDPVR"):
			info["model"] = "TF 7700 HDPVR"
			if fileExists(getPublicPath("/images/boxes/topf.jpg")):
				info["boximage"] = "topf.jpg"
		return info

	def P_epgpop(self, request):
		if "sref" in request.args.keys():
			return getChannelEpg(request.args["sref"][0])
		elif  "sstr" in request.args.keys():
			return getSearchEpg(request.args["sstr"][0])
		else: 
			return []

	def P_screenshot(self, request):
		box = {}
		box['brand'] = "dmm"
		if fileExists("/proc/stb/info/hwmodel"): # box brand
			box['brand'] = "4d"
		elif fileExists("/proc/stb/info/vumodel"):
			box['brand'] = "vuplus"
		elif fileExists("/proc/stb/info/azmodel"):
			box['brand'] = "azbox"
		elif fileExists("/proc/stb/info/gbmodel"):
			box['brand'] = "gigablue"
		return { "box": box }

	def P_powerstate(self, request):
		return {}

	def P_message(self, request):
		return {}

	def P_movies(self, request):
		if "dirname" in request.args.keys():
			movies = getMovieList(request.args["dirname"][0])
		else:
			movies = getMovieList()
		info = getInfo()
		model = info["model"]
		chipset = info["chipset"]
		movies['transcoding'] = False
		if model in ("solo2", "duo2", "solose", "vusolo2", "vuduo2", "vusolose", "xpeedlx3", "gbquad", "gbquadplus") or chipset in ("7356"): # 7356 model default transcoding
			movies['transcoding'] = True
		return movies

	def P_workinprogress(self, request):
		return {}

	def P_radio(self, request):
		return {}

	def P_timers(self, request):
		return getTimers(self.session)

	def P_edittimer(self, request):
		return {}

	def P_tv(self, request):
		return {}

	def P_config(self, request):
		section = "usage"
		if "section" in request.args.keys():
			section = request.args["section"][0]
		return getConfigs(section)

	def P_settings(self, request):
		ret = {
			"result": True
		}
		ret['configsections'] = getConfigsSections()['sections']
		return ret

	def P_multiepg(self, request):
		bouq = getBouquets("tv")
		if "bref" not in request.args.keys():
			bref = bouq['bouquets'][0][0]
		else:
			bref = request.args["bref"][0]

		endtime = 1440
				
		begintime = -1
		day = 0
		if "day" in request.args.keys():
			try:
				day = int(request.args["day"][0])
				now = localtime()
				begintime = mktime( (now.tm_year, now.tm_mon, now.tm_mday+day, 6, 0, 0, -1, -1, -1) )
			except Exception, e:
				pass

		epg = getMultiEpg(self, bref, begintime, endtime)
		epg['bouquets'] = bouq['bouquets']
		epg['bref'] = bref
		epg['day'] = day

		return epg
	def P_multiepg2(self, request):
		reloadtimer = 0
		if "reloadtimer" not in request.args.keys():
			reloadtimer = 1
		bouq = getBouquets("tv")
		if "bref" not in request.args.keys():
			bref = bouq['bouquets'][0][0]
		else:
			bref = request.args["bref"][0]

		endtime = 1440

		begintime = -1
		day = 0
		if "day" in request.args.keys():
			try:
				day = int(request.args["day"][0])
				now = localtime()
				begintime = mktime( (now.tm_year, now.tm_mon, now.tm_mday+day, 6, 0, 0, -1, -1, -1) )
			except Exception, e:
				pass

		epg = getMultiEpg(self, bref, begintime, endtime)
		epg['bouquets'] = bouq['bouquets']
		epg['bref'] = bref
		epg['day'] = day
		epg['reloadtimer'] = reloadtimer

		return epg

	def P_at(self, request):
		ret = {}
		loc = getLocations()
		ret['locations'] = loc['locations']
		return ret

	def P_bqe(self, request):
		ret = {}
		return ret

