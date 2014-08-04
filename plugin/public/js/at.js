//******************************************************************************
//* at.js: openwebif Autotimer plugin
//* Version 1.0
//******************************************************************************
//* Copyright (C) 2014 J�rg Bleyel
//* Copyright (C) 2014 E2OpenPlugins
//*
//* Authors: J�rg Bleyel <jbleyel # gmx.net>
//* License GPL V2
//* https://github.com/E2OpenPlugins/e2openplugin-OpenWebif/blob/master/LICENSE.txt
//*******************************************************************************

// TODO: backup, restore , some error handler

function toUnixDate(date){
	datea = date.split('.');
	var d = new Date();
	d.setFullYear(datea[2],datea[1]-1,datea[0]);
	d.setHours( 0 );
	d.setMinutes( 0 );
	d.setSeconds( 0 );
	return Math.floor(d.getTime() / 1000);
}

function initValues () {

	var _sel1 = $('#oafter');
	var _sel2 = $('#obefore');
	var _sel3 = $('#maxduration');
	var _sel4 = $('#counter');
	var _sel5 = $('#left');

	for (x=0;x<100;x++)
	{
		var sx=x.toString();
		if(x<10)
			sx='0'+sx;
		_sel1.append($('<option></option>').val(x).html(sx));
		_sel2.append($('<option></option>').val(x).html(sx));
		_sel4.append($('<option></option>').val(x).html(sx));
		_sel5.append($('<option></option>').val(x).html(sx));
	}

	for (x=0;x<1000;x++)
	{
		var sx=x.toString();
		if(x<10)
			sx='0'+sx;
		_sel3.append($('<option></option>').val(x).html(sx));
	}
	$('#oafter').val('5');
	$('#obefore').val('5');
	$('#maxduration').val('70');

	var _dateb = new Date();
	var _db = $.datepicker.formatDate('dd.mm.yy', _dateb);
	$('#before').val(_db);

	var _datea = new Date();
	_datea.setDate(_dateb.getDate()+7);
	var _da = $.datepicker.formatDate('dd.mm.yy', _datea);
	$('#after').val(_da);
	$('#from').val('20:15');
	$('#to').val('23:15');
	$('#aefrom').val('20:15');
	$('#aeto').val('23:15');

	$('#after').datepicker({
	
		closeText: tstr_done,
		monthNames: [tstr_january, tstr_february, tstr_march, tstr_april, tstr_may, tstr_june, tstr_july, tstr_august, tstr_september, tstr_october, tstr_november, tstr_december],
		dayNames: [tstr_sunday, tstr_monday, tstr_tuesday, tstr_wednesday, tstr_thursday, tstr_friday, tstr_saturday, tstr_sunday],
		dayNamesMin: [tstr_su, tstr_mo, tstr_tu, tstr_we, tstr_th, tstr_fr, tstr_sa, tstr_su],
		dateFormat: 'dd.mm.yy',
		onClose: function(dateText, inst) {
			if ($('#after').val() != '' && $(this).datepicker('getDate') < $('#before').datepicker('getDate')) {
				$('#error').text(tstr_start_after_end);
				$('#errorbox').show();
			} else
				$('#errorbox').hide();
		}
	});

	$('#before').datepicker({
		closeText: tstr_done,
		monthNames: [tstr_january, tstr_february, tstr_march, tstr_april, tstr_may, tstr_june, tstr_july, tstr_august, tstr_september, tstr_october, tstr_november, tstr_december],
		dayNames: [tstr_sunday, tstr_monday, tstr_tuesday, tstr_wednesday, tstr_thursday, tstr_friday, tstr_saturday, tstr_sunday],
		dayNamesMin: [tstr_su, tstr_mo, tstr_tu, tstr_we, tstr_th, tstr_fr, tstr_sa, tstr_su],
		dateFormat: 'dd.mm.yy',
		onClose: function(dateText, inst) {
			if ($('#before').val() != '' && $(this).datepicker('getDate') > $('#after').datepicker('getDate')) {
				$('#error').text(tstr_start_after_end);
				$('#errorbox').show();
			}
			else
				$('#errorbox').hide();
		}
	});

	$('.date').each(function(index,element){
		$('<span style="display: inline-block">').addClass('ui-icon ui-icon-calendar').insertAfter(element).position({
			of: element
			,my: 'right top'
			,at: 'right top+2'
		});
	});

	$('.time').each(function(index,element){
		$('<span style="display: inline-block">').addClass('ui-icon ui-icon-clock').insertAfter(element).position({
			of: element
			,my: 'right top'
			,at: 'right top+2'
		});
	});

	$("#bouquets").chosen({disable_search_threshold: 10,no_results_text: "Oops, nothing found!",width: "80%"});
	$("#bouquets").chosen().change( function() {$("#bouquets").val($(this).val());});
	$("#channels").chosen({disable_search_threshold: 10,no_results_text: "Oops, nothing found!",width: "80%"});
	$("#channels").chosen().change( function() {$("#channels").val($(this).val());});
	$("#tags").chosen({disable_search_threshold: 10,no_results_text: "Oops, nothing found!",width: "80%"});
	$("#tags").chosen().change( function() {$("#tags").val($(this).val());});

}

function AddFilter(a,b,c)
{
	var rc = $('#filterlist tr').length;
	var nf = $("#dummyfilter").clone(true);
	nf.show();
	nf.attr({
	'id': 'f' + rc.toString(),
	'name': 'f' + rc.toString()
	});
	
	if(a!="")
		nf.find(".FT").val(a);
	if(b!="") {
		if(b=="dayofweek") {
			nf.find(".FM").val(b);
			nf.find(".FI").hide();
			nf.find(".FS").show().val(c);
		}
		else {
			nf.find(".FM").val(b);
			nf.find(".FS").hide();
			nf.find(".FI").show().val(c);
		}
	}
	nf.appendTo("#filterlist");
}

function checkValues () {

	if ($('#timeSpan').is(':checked') == true)
		$('#timeSpanE').show();
	else
		$('#timeSpanE').hide();

	if ($('#timeSpanAE').is(':checked') == true)
		$('#timeSpanAEE').show();
	else
		$('#timeSpanAEE').hide();

	if ($('#timeFrame').is(':checked') == true)
		$('#timeFrameE').show();
	else
		$('#timeFrameE').hide();

	if ($('#timerOffset').is(':checked') == true)
		$('#timerOffsetE').show();
	else
		$('#timerOffsetE').hide();

	if ($('#maxDuration').is(':checked') == true)
		$('#maxDurationE').show();
	else
		$('#maxDurationE').hide();

	if ($('#Location').is(':checked') == true)
		$('#LocationE').show();
	else
		$('#LocationE').hide();

	if ($('#Bouquets').is(':checked') == true)
		$('#BouquetsE').show();
	else
		$('#BouquetsE').hide();

	if ($('#Channels').is(':checked') == true)
		$('#ChannelsE').show();
	else
		$('#ChannelsE').hide();

	if ($('#Filter').is(':checked') == true)
		$('#FilterE').show();
	else
		$('#FilterE').hide();

	if ($('#afterevent').val() != "")
		$('#AftereventE').show();
	else
		$('#AftereventE').hide();

	if ($('#counter').val() != "0")
		$('#CounterE').show();
	else
		$('#CounterE').hide();

	if ($('#vps').is(':checked') == true)
		$('#vpsE').show();
	else
		$('#vpsE').hide();

}

function InitPage() {

	$('#timeSpan').click(function() { checkValues();});
	$('#timeSpanAE').click(function() { checkValues();});
	$('#timeFrame').click(function() { checkValues();});
	$('#timerOffset').click(function() { checkValues();});
	$('#maxDuration').click(function() { checkValues();});
	$('#Location').click(function() { checkValues();});
	$('#Bouquets').click(function() { checkValues();});
	$('#Channels').click(function() { checkValues();});
	$('#Filter').click(function() { checkValues();});
	$("#AddFilter").click(function(){AddFilter("","","");});
	$('#afterevent').change(function () {checkValues();});
	$('#counter').change(function () {checkValues();});
	$('#vps').change(function () {checkValues();});
	
	initValues ();
	checkValues();
	getData();

	$("#actions").buttonset();
	$("#atbutton0").click(function () { addAT(); });
	$("#atbutton0" ).button({icons: { primary: "ui-icon-plus"}});
	$("#atbutton1").click(function () { delAT(); });
	$("#atbutton1" ).button({icons: { primary: "ui-icon-minus"}});
	$("#atbutton2").click(function () { reloadAT(); });
	$("#atbutton2").button({icons: { primary: "ui-icon-arrowrefresh-1-w"}});
	$("#atbutton3").click(function () { saveAT(); });
	$("#atbutton3").button({icons: { primary: "ui-icon-disk"}});
	$("#atbutton4").click(function () { parseAT(); });
	$("#atbutton5").click(function () { simulateAT(); });
	$("#atbutton6").click(function () { listTimers(); });
	// TODO: icons

	$('#errorbox').hide();
	
	$("#simdlg").dialog({
		modal : true, 
		overlay: { backgroundColor: "#000", opacity: 0.5 }, 
		autoOpen: false,
		title: 'Autotimer Preview',
		width: 600,
		height: 400
	});

	$("#timerdlg").dialog({
		modal : true, 
		overlay: { backgroundColor: "#000", opacity: 0.5 }, 
		autoOpen: false,
		title: 'Timer List',
		width: 600,
		height: 400
	});

}

var atxml;
var BQs;
var CurrentAT = null;
var dencoding = null;

function isBQ(sref)
{
	return (sref.indexOf("FROM BOUQUET") > -1);
}

// parse and create AT List
function Parse() {
	
	$("#atlist").empty();
	$(atxml).find("timer").each(function () {
		$("#atlist").append($("<li></li>").html($(this).attr("name")).addClass('ui-widget-content').data('id',$(this).attr("id")));
	});
	
	var item = $("#atlist").find("li").first();
	if(item) {
		FillAT(item.data('id'));
		item.addClass('ui-selected');
	}
}

function isInArray(array, search) { return (array.indexOf(search) >= 0) ? true : false; }

function getTags()
{
	
	// TODO: Errorhandling
	$.getJSON( "/api/gettags", function( data ) {
		var bqs = data['tags'];
		Ts = [];
		var options = "";
		$.each( bqs, function( key, val ) {
			options += "<option value='" + encodeURIComponent(val) + "'>" + val + "</option>";
			Ts.push(val);
		});
		$("#tags").append( options);
		$('#tags').trigger("chosen:updated");
		
	});
}

function getAllServices()
{
	// TODO: Errorhandling

	$.getJSON( "/api/getallservices", function( data ) {
		var bqs = data['services'];
		var options = "";
		var refs = [];
		$.each( bqs, function( key, val ) {
			var ref = val['servicereference']
			var name = '--';
			jQuery.map(BQs, function(obj) {
				if(obj.servicereference === ref)
					name = obj.servicename;
			});
	
			var slist = val['subservices'];
			var items = [];
		
			$.each( slist, function( key, val ) {
				var ref = val['servicereference']
				if (!isInArray(refs,ref)) {
					refs.push(ref);
					if(ref.substring(0, 4) == "1:0:")
						items.push( "<option value='" + ref + "'>" + val['servicename'] + "</option>" );
				}
			});
		
			if (items.length>0) {
				options += "<optgroup label='" + name + "'>" + items.join("") + "</optgroup>";
			}
		});
		$("#channels").append( options);
		$('#channels').trigger("chosen:updated");
		reloadAT();
	});

}

function getServices()
{

	// TODO: Errorhandling
	$.getJSON( "/api/getservices", function( data ) {
		var bqs = data['services'];
		BQs = [];
		var options = "";
		$.each( bqs, function( key, val ) {
			var ref = val['servicereference']
			options += "<option value='" + encodeURIComponent(ref) + "'>" + val['servicename'] + "</option>";
			BQs.push(val);
		});
		$("#bouquets").append( options);
		$('#bouquets').trigger("chosen:updated");
	});

}


function getData()
{
	// TODO: Errorhandling
	// Timing
	getTags();
	getServices();
	getAllServices();
}


function FillAT(autotimerid)
{
	var def = $(atxml).find("defaults");
	if(def)
		dencoding=def.attr("encoding");
	if(!dencoding)
		dencoding="UTF-8";

	$(atxml).find("timer").each(function () {
		if($(this).attr("id")==autotimerid) {
			CurrentAT = new AutoTimerObj($(this));
			CurrentAT.UpdateUI();
		}
	});
	checkValues ();
}

function AutoTimerObj (xml) {

	this.isNew = false;
	this.MustSave = false;
	this.id = xml.attr("id");
	this.enabled = (xml.attr("enabled") == "yes");

	this.name = xml.attr("name");
	if(!this.name)
		this.name='';

	this.match = xml.attr("match");
	if(!this.match)
		this.match='';

	this.searchType = "partical";
	if(xml.attr("searchType"))
		this.searchType=xml.attr("searchType");

	this.searchCase = "insensitive";
	if(xml.attr("searchCase"))
		this.searchCase=xml.attr("searchCase");

	this.justplay = "0";
	if(xml.attr("justplay"))
		this.justplay=xml.attr("justplay");

	this.overrideAlternatives = (xml.attr("overrideAlternatives") == "1");

	
	this.timeSpan = false;
	if(xml.attr("from") && xml.attr("to"))
	{
		this.from = xml.attr("from");
		this.to = xml.attr("to");
		this.timeSpan = true;
	}

	this.maxduration=null;
	if(xml.attr("maxduration")) 
		this.maxduration=xml.attr("maxduration");
	
	if(xml.attr("after") && xml.attr("before"))
	{
		var _i=parseInt(xml.attr("after"));
		var _date = new Date(_i*1000);
		var _dt = $.datepicker.formatDate('dd.mm.yy', _date);
		this.after = _dt;

		_i=parseInt(xml.attr("before"));
		_date = new Date(_i*1000);
		_dt = $.datepicker.formatDate('dd.mm.yy', _date);
		this.before = _dt;
		this.timeFrame=true;
	}
	else
	{
		this.before=null;
		this.after=null;
		this.timeFrame=false;
	}

	this.avoidDuplicateDescription="0";
	if(xml.attr("avoidDuplicateDescription"))
		this.avoidDuplicateDescription=xml.attr("avoidDuplicateDescription")

	this.location=null;
	if(xml.attr("location")) 
		this.location = xml.attr("location");

	this.timerOffset=false;
	if(xml.attr("offset"))
	{
		var fields = xml.attr("offset").split(',');
		var _b = fields[0];
		var _a = fields[1];
		if (typeof _a === "undefined") {
			this.timerOffsetAfter=_b;
			this.timerOffsetBefore=_b;
		} else {
			this.timerOffsetAfter=_a;
			this.timerOffsetBefore=_b;
		}
		this.timerOffset=true;
	}
	
	var _ae = xml.find('afterevent');
	this.afterevent=null;
	if(_ae.text())
	{
		this.afterevent=_ae.text();
		if(_ae.attr("from") && _ae.attr("to"))
		{
			this.aftereventfrom = _ae.attr("from");
			this.aftereventto = _ae.attr("to");
		}
		else
		{
			this.aftereventfrom=null;
			this.aftereventto=null;
		}
	}

	var _c = [];
	var _b = [];
	xml.find("e2service").each(function () {
		var ref = $(this).find("e2servicereference").text();
		if (isBQ(ref))
			_b.push(encodeURIComponent(ref));
		else
			_c.push(ref);
	});
	
	this.Channels = _c.slice();
	this.Bouquets = _b.slice();

	// Tags
	_b = [];
	xml.find("e2tags").each(function () {
		var tag = $(this).text();
		_b.push(encodeURIComponent(tag));
	});

	this.Tags = _b.slice();
	
	// Filters
	var _f = [];
	
	xml.find("include").each(function () {
		_f.push (
			{ 	"t" : "include",
				"w": $(this).attr("where"),
				"v": $(this).text()
			}
		); 
	});

	xml.find("exclude").each(function () {
		_f.push (
			{ 	"t" : "exclude",
				"w": $(this).attr("where"),
				"v": $(this).text()
			}
		); 
	});

	this.Filters = _f.slice();

	this.counter = xml.attr("counter");
	if(!this.counter)
		this.counter='0';

	this.left = xml.attr("left");
	if(!this.left)
		this.left='0';

	this.counterFormat = xml.attr("counterFormat");
	if(!this.counterFormat)
		this.counterFormat='';

	this.encoding = xml.attr("encoding");
	if(!this.encoding) {
		this.encoding = dencoding;
	}

	this.vps = false;
	this.vpso = false;
	if(xml.attr("vps_enabled") === "yes") {
		this.vps = true;
		if(xml.attr("vps_overwrite") === "yes") {
			this.vpso = true;
		}
	}

}

AutoTimerObj.prototype.UpdateUI = function(){
	$('#enabled').prop('checked', this.enabled); 
	$('#name').val(this.name);
	$('#match').val(this.match);
	$('#searchType').val(this.searchType);
	$('#searchCase').val(this.searchCase);
	$('#justplay').val(this.justplay);
	$('#overrideAlternatives').prop('checked', this.overrideAlternatives); 
	$('#timeSpan').prop('checked',this.timeSpan);

	$('#at_name').html("(" + this.name +")");

	if(this.timeSpan)
	{
		$('#from').val(this.from);
		$('#to').val(this.to);
	}
	
	if(this.maxduration)
	{
		$('#maxDuration').prop('checked',true);
		$('#maxduration').val(this.maxduration);
	}
	else
		$('#maxDuration').prop('checked',false);

	$('#timeFrame').prop('checked',this.timeFrame);
	if(this.timeFrame)
	{
		$('#after').val(this.after);
		$('#before').val(this.before);
	}

	$("#avoidDuplicateDescription").val(this.avoidDuplicateDescription);
	
	if(this.location) {
		$('#location').val(this.location);
		$('#Location').prop('checked',true);
	}
	else
		$('#Location').prop('checked',false);

	$('#timerOffset').prop('checked',this.timerOffset);
	if(this.timerOffset)
	{
		$('#oafter').val(this.timerOffsetAfter);
		$('#obefore').val(this.timerOffsetBefore);
	}

	$('#timeSpanAE').prop('checked',false);
	$('#afterevent').val("");
	if(this.afterevent) {
		$('#afterevent').val(this.afterevent);
		if(this.aftereventfrom && this.aftereventto) {
			$('#aefrom').val(this.aftereventfrom);
			$('#aeto').val(this.aftereventto);
			$('#timeSpanAE').prop('checked',true);
		}
	}
	
	$.each(this.Bouquets, function(index, value) {
		$('#bouquets option[value="' + value + '"]').prop("selected", true);
	});
	
	$.each(this.Channels, function(index, value) {
		$('#channels option[value="' + value + '"]').prop("selected", true);
	});

	$('#Bouquets').prop('checked',(this.Bouquets.length>0));
	$('#Channels').prop('checked',(this.Channels.length>0));
	
	if(this.Bouquets.length==0)
		$('#bouquets').val(null);
	if(this.Channels.length==0)
		$('#channels').val(null);

	$('#tags').val(null);
	$.each(this.Tags, function(index, value) {
		$('#tags option[value="' + value + '"]').prop("selected", true);
	});

	$('#bouquets').trigger("chosen:updated");
	$('#channels').trigger("chosen:updated");
	$('#tags').trigger("chosen:updated");

	var rc = $('#filterlist tr').length;
	if(rc>1)
	{
		for(var x=1;x<rc;x++)
			$('#f' + x.toString()).remove();
	}
	var c=0;
	$.each(this.Filters, function(index, value) {
		c++;
		AddFilter(value.t,value.w,value.v);
	});
	$('#Filter').prop('checked',(c>0));
	
	$('#counter').val(this.counter);

	$('#left').val(this.left);
	
	$('#counterFormat').val(this.counterFormat);
	
	$('#vps').prop('checked',this.vps);

	$('#vpso').prop('checked',this.vpso);
	
	checkValues();
};

function addAT()
{

	if(CurrentAT && CurrentAT.isNew)
	{
		showError("please save the current autotimer first");
		return;
	}
	var _id=1;
	
	$(atxml).find("timer").each(function () {
		var li = parseInt($(this).attr("id"));
		if(li>=_id)
			_id=li+1;
	});

	var name = "New Name";
	var match = "New Name";
	var id = _id.toString();

	var xml = '<timers><timer name="'+name+'" match="'+match+'" enabled="yes" id="'+id+'" encoding="ISO8859-15"></timer></timers>',
	xmlDoc = $.parseXML( xml )
	
	$(xmlDoc).find("timer").each(function () {
		$( "#atlist" ).append($('<li></li>').html($(this).attr("name")).addClass('ui-widget-content').data('id',$(this).attr("id")));
		CurrentAT = new AutoTimerObj($(this));
		CurrentAT.isNew = true;
		CurrentAT.MustSave = true;
		CurrentAT.UpdateUI();
	});
	
	$('#atlist').find('li').each(function () {
		if($(this).data('id') == id)
			$(this).addClass('ui-selected');
		else
			$(this).removeClass('ui-selected');
	});
	
}

function delAT()
{

	if(CurrentAT && !CurrentAT.isNew)
	{
		if(confirm("Do you really want to delete the AT (" + CurrentAT.title + ") ?") === false)
			return;
		$.ajax({
			type: "GET", url: "/autotimer/remove?id=" + CurrentAT.id,
			dataType: "xml",
			success: function (xml)
			{
			
				var state=$(xml).find("e2state").first();
				var txt=$(xml).find("e2statetext").first();
				
				showError(txt.text());
				
				console.debug(xml);
				readAT();
			},
			error: function (request, status, error) {
				showError(request.responseText);
			}
		});
		
	}
}

function readAT()
{
	CurrentAT = null;
	$.ajax({
		type: "GET", url: "/autotimer",
		dataType: "xml",
		success: function (xml)
		{
			atxml=xml;
			Parse();
		},error: function (request, status, error) {
			showError(request.responseText);
			// TODO : error handling
		}
	});
}

function saveAT()
{
	// TODO: set mustsave
	if(CurrentAT) // && CurrentAT.MustSave)
	{

	var reqs = "/autotimer/edit?";

	CurrentAT.enabled = $('#enabled').is(':checked');
	CurrentAT.name = $('#name').val();
	CurrentAT.match = $('#match').val();
	CurrentAT.searchType = $('#searchType').val();
	CurrentAT.searchCase = $('#searchCase').val();
	CurrentAT.justplay = $('#justplay').val();
	CurrentAT.justplay = $('#justplay').val();
	CurrentAT.overrideAlternatives = $('#overrideAlternatives').is(':checked');
	CurrentAT.timeSpan = $('#timeSpan').is(':checked');
	CurrentAT.avoidDuplicateDescription = $('#avoidDuplicateDescription').val();
	CurrentAT.location = $('#avoidDuplicateDescription').val();
	CurrentAT.timeSpan = $('#timeSpan').is(':checked');
	CurrentAT.from = $('#from').val();
	CurrentAT.to = $('#to').val();

	if($('#maxDuration').is(':checked')) {
		CurrentAT.maxduration = $('#maxduration').val();
	}
	else
		CurrentAT.maxduration = null;

	if($('#Location').is(':checked'))
		CurrentAT.location = $('#location').val();
	else
		CurrentAT.location = null;

	CurrentAT.timeFrame = $('#timeFrame').is(':checked');
	CurrentAT.timerOffsetBefore = $('#obefore').val();
	CurrentAT.timerOffsetAfter = $('#oafter').val();

	CurrentAT.afterevent = $('#afterevent').val();
	CurrentAT.aftereventfrom = $('#aefrom').val();
	CurrentAT.aftereventto = $('#aeto').val();

	CurrentAT.Bouquets = $("#bouquets").chosen().val();
	CurrentAT.Channels = $("#channels").chosen().val();

	
	var _f = [];

	$.each($('#filterlist tr'), function(index, value) {
		var tr = $(value);
		if(tr.prop('id') !== "dummyfilter") {
			var FT = tr.find(".FT");
			var FM = tr.find(".FM");
			var FI = tr.find(".FI");
			var FS = tr.find(".FS");
			
			if (FM.val() === 'dayofweek'){
				_f.push (
						{ 	"t" : FT.val(),
							"w": FM.val(),
							"v": FS.val()
						}
					); 
			}
			else {
				_f.push (
						{ 	"t" : FT.val(),
							"w": FM.val(),
							"v": FI.val()
						}
					); 
				
			}
		}
	});

	CurrentAT.Filters = _f.slice();
	
	CurrentAT.Tags = $("#tags").chosen().val();

	CurrentAT.counter = $('#counter').val();
	CurrentAT.left = $('#left').val();
	CurrentAT.counterFormat = $('#counterFormat').val();
	CurrentAT.vps = $('#vps').is(':checked');
	CurrentAT.vpso = $('#vpso').is(':checked');

	
	reqs += "match=" + encodeURIComponent(CurrentAT.match);
	reqs += "&name=" + encodeURIComponent(CurrentAT.name);
	reqs += "&enabled=";
	reqs += (CurrentAT.enabled) ? "1" : "0";
	reqs += "&justplay=";
	reqs += (CurrentAT.justplay) ? "1" : "0";
	reqs += "&setEndtime=";
	reqs += (CurrentAT.setEndtime) ? "1" : "0";
	reqs += "&searchCase=" + CurrentAT.searchCase;
	reqs += "&overrideAlternatives=";
	reqs += (CurrentAT.overrideAlternatives) ? "1" : "0";
	reqs += "&avoidDuplicateDescription=" + CurrentAT.avoidDuplicateDescription;
	// TODO:
	//	reqs += "&searchForDuplicateDescription=" + CurrentAT.searchForDuplicateDescription;
	if(CurrentAT.location)
		reqs += "&location=" + encodeURIComponent(CurrentAT.location);
	reqs += "&searchType=" + CurrentAT.searchType;
	reqs += "&maxduration=";
	if(CurrentAT.maxduration && CurrentAT.maxduration > -1)
		reqs += CurrentAT.maxduration;
	reqs += "&encoding=" + encodeURIComponent(CurrentAT.encoding);

	if(CurrentAT.timerOffsetAfter > -1 && CurrentAT.timerOffsetBefore > -1)
		reqs += "&offset=" + CurrentAT.timerOffsetBefore + "," + CurrentAT.timerOffsetAfter;
	else
		reqs += "&offset=";

	if(CurrentAT.timeSpan)
		reqs += "&timespanFrom=" + CurrentAT.from + "&timespanTo=" + CurrentAT.to;
	else
		reqs += "&timespanFrom=&timespanTo=";

	if(CurrentAT.timeFrame)
		reqs += "&before=" + toUnixDate(CurrentAT.before) + "&after=" + toUnixDate(CurrentAT.after);
	else
		reqs += "&before=&after=";

	if(CurrentAT.Tags && CurrentAT.Tags.length > 0) {
		$.each( CurrentAT.Tags, function( index, value ){
			reqs += "&tag=" + value;
		});
	} else
		reqs += "&tag=";

	reqs += "&services=";
	if(CurrentAT.Channels && CurrentAT.Channels.length > 0) {
		var _s = [];
		$.each( CurrentAT.Channels, function( index, value ){
			_s.push(encodeURIComponent(value));
		});
		reqs += _s.join(',');
	}

	reqs += "&bouquets=";
	if(CurrentAT.Bouquets && CurrentAT.Bouquets.length > 0) {
		reqs += CurrentAT.Bouquets.join(',');
	}

	
	if(CurrentAT.Filters && CurrentAT.Filters.length > 0) {
		$.each( CurrentAT.Filters, function( index, value ){
			var fr = "&"
			if(value.t === "exclude")
				fr+="!";
			fr += value.w;
			fr += "=";
			if (value.w === 'dayofweek')
				fr += value.v;
			else
				fr += encodeURIComponent(value.v);
			reqs += fr;
		});
	}

	if(!CurrentAT.vps)
		CurrentAT.vpo=false;

	reqs += "&vps_enabled=";
	reqs += (CurrentAT.vps) ? "1" : "0";
	
	reqs += "&vps_overwrite=";
	reqs += (CurrentAT.vpso) ? "1" : "0";

	if(!CurrentAT.isNew)
		reqs += "&id=" + CurrentAT.id;
		
		$.ajax({
			type: "GET", url: reqs,
			dataType: "xml",
			success: function (xml)
			{
				var state=$(xml).find("e2state").first();
				var txt=$(xml).find("e2statetext").first();
				showError(txt.text(),state.text());
				readAT();
			},
			error: function (request, status, error) {
				showError(request.responseText);
			}
		});
		
	}
}

function simulateAT()
{
	$.ajax({
		type: "GET", url: "/autotimer/simulate",
		dataType: "xml",
		success: function (xml)
		{
			var lines= [];
			$(xml).find("e2simulatedtimer").each(function () {
				var line = '<tr>';
				line += '<td>' + $(this).find('e2autotimername').text() + '</td>';
				line += '<td>' + $(this).find('e2name').text() + '</td>';
				line += '<td>' + $(this).find('e2servicename').text() + '</td>';
				var s = $(this).find('e2timebegin').text();
				var d = new Date(Math.round(s) * 1000)
				s = (d.getMonth()+1) + '/' + d.getDate() + '/' + d.getFullYear() + ' ' + d.getHours() + ':' + d.getMinutes();
				line += '<td>' + s + '</td>';
				s = $(this).find('e2timeend').text();
				d = new Date(Math.round(s) * 1000)
				s = (d.getMonth()+1) + '/' + d.getDate() + '/' + d.getFullYear() + ' ' + d.getHours() + ':' + d.getMinutes();
				line += '<td>' + s + '</td>';
				line += '</tr>';
				lines.push(line);
			});
			
			$("#simtb").empty();
			$(lines).each(function(idx,val) {
				$("#simtb").append(val);
			});
			if(lines.length===0)
				$("#simtb").append("<tr><td COLSPAN=5>NO Timer found</td></tr>");
			$("#simdlg").dialog( "open" );

		},
		error: function (request, status, error) {
			showError(request.responseText);
		}
	});
}

function parseAT()
{
	$.ajax({
		type: "GET", url: "/autotimer/parse",
		dataType: "xml",
		success: function (xml)
		{
			var state=$(xml).find("e2state").first();
			var txt=$(xml).find("e2statetext").first();
			showError(txt.text(),state.text());
		},
		error: function (request, status, error) {
			showError(request.responseText);
		}
	});
}

function reloadAT()
{
	showError("");
	readAT();
	$( "#atlist" ).selectable({
		selected: function( event, ui ) {
			var ids = $('#atlist .ui-selected').map(function() {
				FillAT($(this).data('id'));
			});
		}
	});

}

function listTimers()
{
	$("#timerdlg").dialog( "open" );
	$("#timerdlgcont").html(loadspinner).load('ajax/timers #timers', function() {
		$("#timerdlgcont #timers .moviecontainer_main .moviecontainer_right div a:first").hide();
	});
}
function showError(txt,st)
{
	st = typeof st !== 'undefined' ? st : "False";
	$('#success').text("");
	$('#error').text("");
	if(st === "True")
		$('#success').text(txt);
	else
		$('#error').text(txt);
	if(txt!=="")
		$('#errorbox').show();
	else
		$('#errorbox').hide();
}

