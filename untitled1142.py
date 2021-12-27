# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:28:33 2021

@author: Administrator
"""

import urllib.request as ur
import requests
# import BeautifulSoup

from bs4 import BeautifulSoup
data='''

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

<title>公開資訊觀測站</title>
<link href="css/css1.css" rel="stylesheet" type="text/css" Media="Screen"/>
<link href="css/print_css1.css" rel="stylesheet" type="text/css" Media="Print"/>
<link href="css/clickmenu.css"rel="stylesheet" type="text/css"/>

<script type="text/javascript" src="js/mops1.js"></script>

<script type="text/javascript" src="js/jquery-1.1.4.pack.js"></script>
<script type="text/javascript" src="js/jquery.clickmenu.js"></script>


</head>
<body>

<center>
<table border="0"><tr><td align="left">
<form name='fh' style='margin:0;' action='/mops/web/ajax_autoComplete' method='post' onsubmit='return false;'><input type='hidden' name='firstin' id='firstin' value = '1'><input type='hidden' name='TYPEK' id='TYPEK' value = 'all'><input type='hidden' name='step' id='step' value = '1'><input type='hidden' name='co_id' value = ''><input type='hidden' name = 'funcName' value = 't163sb04'><input type='hidden' name='searchtype' id='searchtype' value = ''><input type='hidden' name='inpuType' id='inpuType' value = 'keyword'><input type='hidden' name='auto-more' id='auto-more' value = ''><input type = 'hidden' name = 'keycon' value = ''><div id='head'><div id='head_02'><a href='/mops/web/index' alt='回首頁'><img src='images/blank.gif' width='232' height='52' border='0'></a></div><div id='head_03'><div id='search_bar'><div id='nav'><a style='color:yellow;text-decoration:none;'>全站搜尋</a></div><div id='search_b1' align='left'><table><tr><td align='left'><input name='keyword' type='text' class='textbox' id='keyword' size='45' oninput="document.getElementById('auto-more').value='';autoComplete(this.form , 'keyword' , 'auto-complete-data' , event);" onkeydown='chkKeyDown(this.form , this , "auto-complete-data" , event);' onkeyUp="document.getElementById('auto-more').value='';autoComplete(this.form , 'keyword' , 'auto-complete-data' , event);" onblur="setTimeout(function(){hideDiv('auto-complete-data');} , 200);" onClick="this.value='';document.getElementById('oldKeyWord').value='';hideDiv('auto-complete-data');" placeholder='請輸入公司代號、簡稱，或報表關鍵字' autocomplete='off'></td><td><input type='button' name='rulesubmit' id='rulesubmit' value=' 搜尋 ' onclick="document.fh.action='/mops/web/autoAction';document.fh.submit();"></td></tr></table></div><div id='search_txt' class='search_b2' style='z-index:1;'><table border='0'><tr><td><div style='background-image: url(images/map01.jpg) ; height: 19px; width:32px;background-position:-161px 0px;'></div></td><td><a href='javascript:void(0);' onClick='document.fh.keyword.value="營收";goaction("營收" , "0");'>營收</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="除權息";goaction("除權息" , "0");'>除權息</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="電子書";goaction("電子書" , "0");'>電子書</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="法說會";goaction("法說會" , "0");'>法說會</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="庫藏股";goaction("庫藏股" , "0");'>庫藏股</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="董監持股";goaction("董監持股" , "0");'>董監持股</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="獨立董事";goaction("獨立董事" , "0");'>獨立董事</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="董監酬金";goaction("董監酬金" , "0");'>董監酬金</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="ETF";goaction("ETF" , "0");'>ETF</a><a href='javascript:void(0);' onClick='document.fh.keyword.value="TDR";goaction("TDR" , "0");'>TDR</a></td></tr></table></div></div></div><div id='head_04'><a href='http://emops.twse.com.tw/emops_all.htm'><img src='images/blank.gif' width='89' height='32' border='0' /></a><p><a href='/mops/web/index'><img src='images/blank.gif' width='89' height='32' border='0' /></a></div></div></form><input type='hidden' id='oldKeyWord'><div id='auto-complete-data'></div><div id='auto-complete-data2'></div><form name='fh2' style='margin:0;' action='' method='post' onsubmit='return false;'><input type='hidden' name='usually' id='usually' value = ''></form><script>window.onload=getMsg;    var MAR = document.querySelector("#marquee");     if(MAR){         var MARS = document.querySelectorAll("#marquee a");         for(var i=0;i<MARS.length;i++){             MARS[i].setAttribute("target","_blank");             MARS[i].setAttribute("style","margin-right:20px");         };         if(MARS.length<1){             MAR.parentNode.innerHTML = "<span style='color:#ff0;'>全站搜尋</span>";             MAR.setAttribute("scrollamount","0")         };     };</script><style>    #marquee,#marquee a{color: #ff0!important;}    #marquee a:hover{color: #ff0!important;text-decoration: none!important;}    #marquee a[href]{text-decoration: underline!important;}</style> 



<div id="menu" class="clickMenu">
	<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<script>
			$(document).ready(function() {
			
				$('#list').clickMenu();
				document.getElementById('list').style.display='block';
			});
		</script> 
		<tr>
			<td id="menu1">
				<ul id="list" style="display:none;">
					<li class = "L00_Pop" id="mm0">常用報表
					</li>
					<li class = "L00_Pop" id="mm1">基本資料
					</li>
					<li class = "L00_Pop" id="mm2">彙總報表
					</li>
					<li class = "L00_Pop" id="mm3">股東會及股利
					</li>
					<li class = "L00_Pop" id="mm4">公司治理
					</li>
					<li class = "L00_Pop" id="mm5">財務報表
					</li>
					<li class = "L00_Pop" id="mm6">重大訊息與公告
					</li>
					<li class = "L00_Pop" id="mm7">營運概況
					</li>
					<li class = "L00_Pop" id="mm8">投資專區
					</li>
					<li class = "L00_Pop" id="mm9">認購（售）權證
					</li>
					<li class = "L00_Pop" id="mm10">債券
					</li>
					<li class = "L00_Pop" id="mm11">資產證券化
					</li>

				</ul>
			</td>
		</tr>
	</table>
</div>






<div id="maincontent_in">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td >
<div id="PageBody">
<table><tr><td valign="top" style="height:400px">
<div id="main" >

<!-- 
	程式名稱:submenu-2.htm
	程式功能:submenu-2.htm
	修改紀錄:(格式=>西元日期+版次+程式設計師)
	2021071441twse1097(T88K)新增t163sb20現金流量表
	2021071245twse1097(T88G)新增t163sb20現金流量表
	2019092740:hsin(T88K)轉換公司債轉換變動情形一覽表t98sb05改到基本資料，IFRSs後每月營業收入彙總表t21sc04_ifrs上移一層
	2019092744:hsin(T88G)轉換公司債轉換變動情形一覽表t98sb05改到基本資料，IFRSs後每月營業收入彙總表t21sc04_ifrs上移一層
	2019040843ivy:(T88G)增加普通股股利分派頻率及決議層級彙總表
	2017032142thomas:(T88G)修改t06sf09_2_q1,t163sb11標題文字
	2016121960oliver:(T88G)
		1.「董事及監察人出(列)席董事會及進修情形與獨立董事兼任情形(個別) 」t100sb07移至「內部控制專區」及「獨立董監事兼任情形彙總表」之間，並更名為「董事及監察人出(列)席董事會及進修情形與暨獨立董事現職、經歷及兼任情形(個別) 」。
		2. 「獨立董監事兼任情形彙總表」t93sc01_1更名為「獨立董監事現職、經歷及兼任情形彙總表」
		3.  「董事及監察人出(列)席董事會及進修情形」t93sc03_1更名為「董事及監察人出(列)席董事會及進修情形彙總表」
		4. 「財務報告經監察人承認情形」刪除。(與彙總報表／財務報表重複)
		5. 「採累積投票制、全額連記法、候選人提名制選任董監事及當選資料彙總表」更名為「採候選人提名制、累積投票制、全額連記法選任董監事及當選資料彙總表」
		6. 「採候選人提名制、累積投票制、全額連記法選任董監事及當選資料彙總表」t144sb11、「股東行使提案權情形彙總表」t144sb09及「股東會議案決議情形」t150sb04移至「彙總報表／股東會及股利」項下，依前三項順序介於「股東會公告」及「股利分派情形」之間
		2019042939ivy:(T88K)增加普通股股利分派頻率及決議層級彙總表
	2017032138thomas:(T88K)修改t06sf09_2_q1,t163sb11標題文字
	2016123037oliver:(T88K)
	2015122936edward:(T88K)修改t66sb06名稱
	2015122935edward:(T88K)修改t66sb06名稱
	2015072934:thomas:(T88K)增加 t06sf09_1_q1「截至各季綜合損益財測達成情形(完整式)」。
	2015060533thomas:(T88K)新增 t163sb11,t163sb12
	2014102832thomas:修改原為「召開股東常(臨時)會日期、地點資料彙總表」改為「召開股東常(臨時)會日期、地點及採用電子投票情形等資料彙總表」。
	2014041431kevin:(T88K)新增t158sb06
	2014032830kevin:(T88K)新增t163sb19
	2013121228edward:(T88K)增加t116sb01_new
	2013051027:leo:(T88K)修改選單排列
	2013043026:leo:(T88K)新增t56sb29_q3,t163sb14
	2013041225:leo:(T88K)新增t66sb06
	2013032024:leo:(T88K)財務預測,財務報表拆為IFRSs前後
	2013013123:leo:(T88K)新增t06sf09_1_q1 t06sf09_2_q1 t06sf09_3_q1
	2012122922:tobey:(T88K)將財務比率分析拆為IFRSs前後
	2012111221:leo:(T88K)新增合併損益表，合併資產負債表
	2012101820:leo:(T88K)修改庫藏股統計表文字,連結
	2012052919:tobey:(T88K)新增t160sb04
	2012021718:lucas:新增t66sb23
	2012020115:lucas:刪除內部公告聲明書和專案書(t06sg20,t06hsg20)
	2011100414:draco :新增t132sb21,t132sb22
	2011030813:edward:(T88K)新增t21sb06
-->
<table width="176" border="0" cellpadding="0" cellspacing="0">
<tr>
	<td width="176">
		<span style="cursor: pointer; font-weight: bold; font-size: 13px;" onclick="showhide('level2','img-2')" id="menu1"> 
			<img src="images/minus4.gif" id="img-2"/><a href="#">彙總報表</a>
		</span>
	</td>
</tr>
<tr style="display: inline;" id="level2">
	<td style="padding-left: 10px;">
		<img src="images/minus3.gif" id="img-2001"/>
			<a onclick="showhide('level-2001','img-2001')" target="_self" href="#">基本資料</a><br/>
			<span style="display: none;" id="level-2001">
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t51sb01">基本資料查詢彙總表</a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t79sb04">重要子公司基本資料彙<br/><span style="padding-left: 30px;">總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t47hsc01">國內公司發行海外存託<br/><span style="padding-left: 30px;">憑證彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t35sb00_6">庫藏股統計表(已移至「<br/><span style="padding-left: 30px;">投資專區」項下「庫<br/></span><span style="padding-left: 30px;">藏股資訊專區」)</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t51sb04_q1">員工認股權憑證基本資<br/><span style="padding-left: 30px;">料彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t158sb06">員工認股權憑證實際發<br/><span style="padding-left: 30px;">行資料及已(未)執行認<br/></span><span style="padding-left: 30px;">股情形彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t160sb04">限制員工權利新股基本<br/><span style="padding-left: 30px;">資料彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t51sb04_q2">國內其他有價證券資料<br/><span style="padding-left: 30px;">彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t51sb03">海外有價證券基本資料<br/><span style="padding-left: 30px;">彙總表</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t98sb05">轉換公司債轉換變動情<br/><span style="padding-left: 30px;">形一覽表</span></a><br/>
				</span>
			</span>
			
		<img src="images/minus3.gif" id="img-2002"/>
			<a onclick="showhide('level-2002','img-2002')" target="_self" href="#">股東會及股利</a><br/>
			<span style="display: none;" id="level-2002">
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2002001"/>
					<a onclick="showhide('level-2002001','img-2002001')" target="_self" href="#">股東會公告</a><br/>
					<span style="display: none;" id="level-2002001">
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t108sb31_q1">召開股東常（臨時<br/><span style="padding-left: 52px;">）會日期、地點及</span><br/><span style="padding-left: 52px;">採用電子投票情</span><br/><span style="padding-left: 52px;">形等資料彙總表</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t108sb26">召集股東常（臨時<br/><span style="padding-left: 52px;">）會公告資料彙總</span><br/><span style="padding-left: 52px;">表（95年度起適</span><br/><span style="padding-left: 52px;">用）</span></a><br/>
						</span>
					</span>
				</span>

				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t144sb11">採候選人提名制、<br/><span style="padding-left: 30px;">累積投票制、<br/></span>
					<span style="padding-left: 30px;">全額連記法選任</span><br/><span style="padding-left: 30px;">董監事及當選</span><br/><span style="padding-left: 30px;">資料彙總表</span></a><br/>
				</span>

				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t144sb09">股東行使提案權情形<br/><span style="padding-left: 30px;">彙總表</span></a><br/>
				</span>

				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t150sb04">股東會議案決議情形</a>
				</span>
			
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t05sb12">普通股股利分派頻率<br/><span style="padding-left: 30px;">暨普通股年度(含第4季<br/><span style="padding-left: 30px;">或後半年度)現金股息<br/><span style="padding-left: 30px;">及紅利決議層級彙總表</a><br/>
				</span>

				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t05st09_new">股利分派情形</a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t66sb06">僅分派員工紅利及董監<br/><span style="padding-left: 30px;">酬勞而未分派股利之公<br/><span style="padding-left: 30px;">司查詢(自104年度起不<br/><span style="padding-left: 30px;">適用)</a><br/></span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t66sb23">TDR股利分派情形(101<br/><span style="padding-left: 30px;">年起適用)</a><br/></span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t108sb27">除權息公告</a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t108sb31new">股東會及除權息日曆</a><br/>
				</span>
			</span>
			
		<img src="images/pointer.gif"/><a href="t100sb02_1">法人說明會一覽表</a><br/>
		
		<img src="images/minus3.gif" id="img-2004"/>
			<a onclick="showhide('level-2004','img-2004')" target="_self" href="#">財務報表</a><br/>
			<span style="display: none;" id="level-2004">
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2004001"/>
					<a onclick="showhide('level-2004001','img-2004001')" target="_self" href="#">採IFRSs後</a><br/>
					<span style="display: none;" id="level-2004001">
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t163sb04">綜合損益表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t163sb05">資產負債表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t163sb20">現金流量表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t56sb29_q3">財務報告經<br/><span style="padding-left: 52px;">監察人承認</span><br/><span style="padding-left: 52px;">情形</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t163sb14">會計師查核<br/><span style="padding-left: 52px;">(核閱)報告</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t163sb19">各產業EPS<br/><span style="padding-left: 52px;">統計資訊</span></a><br/>
						</span>
					</span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2004002"/>
					<a onclick="showhide('level-2004002','img-2004002')" target="_self" href="#">採IFRSs前</a><br/>
					<span style="display: none;" id="level-2004002">
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t51sb08">損益表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t51sb07">資產負債表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t51sb13">合併損益表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t51sb12">合併資產負債表</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t132sb21">第一上市櫃損益季<br/><span style="padding-left: 52px;">節查詢彙總表</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t132sb22">第一上市櫃資產負<br/><span style="padding-left: 52px;">債季節查詢彙總表</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t56sb29_q2">財務報告經監察人<br/><span style="padding-left: 52px;">承認情形</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t06se09_1">會計師查核(核閱)報<br/><span style="padding-left: 52px;">告</span></a><br/>
						</span>
					</span>
				</span>
			</span>

		<img src="images/minus3.gif" id="img-2005"/>
			<a onclick="showhide('level-2005','img-2005')" target="_self" href="#">財務預測</a><br/>
			<span style="display: none;" id="level-2005">
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2005001"/>
					<a onclick="showhide('level-2005001','img-2005001')" target="_self" href="#">採IFRSs後</a><br/>
					<span style="display: none;" id="level-2005001">
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005001001"/><a onclick="showhide('level-2005001001','img-2005001001')" target="_self" href="#">財測達成情形</a><br/>
							<span style="display: none;" id="level-2005001001">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_1_q1">截至各季綜合損<br/><span style="padding-left: 69px;">益財測達成情形</span><br/><span style="padding-left: 69px;">(完整式)</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t163sb11">年度自結綜合損<br/><span style="padding-left: 69px;">益達成情形(完</span><br/><span style="padding-left: 69px;">整式)</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t163sb12">年度實際綜合損<br/><span style="padding-left: 69px;">益(經會計師查</span><br/><span style="padding-left: 69px;">核)達成情形<br/><span style="padding-left: 69px;">(完整式)</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_2_q1">各季綜合損益財<br/><span style="padding-left: 69px;">測達成情形(簡</span><br/><span style="padding-left: 69px;">式)</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_3_q1">當季綜合損益經<br/><span style="padding-left: 69px;">會計師查核(核</span><br><span style="padding-left: 69px;">閱)數與當季預</span><br/><span style="padding-left: 69px;">測數差異達百分</span><br/><span style="padding-left: 69px;">之十以上者，或</span><br/><span style="padding-left: 69px;">截至當季累計差</span><br/><span style="padding-left: 69px;">異達百分之二十</span><br><span style="padding-left: 69px;">以上者(簡式)</span></a><br/>
								</span>
							</span>
						</span>
					</span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2005002"/>
					<a onclick="showhide('level-2005002','img-2005002')" target="_self" href="#">採IFRSs前</a><br/>
					<span style="display: none;" id="level-2005002">
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005002001"/><a onclick="showhide('level-2005002001','img-2005002001')" target="_self" href="#">財測達成情形</a><br/>
							<span style="display: none;" id="level-2005002001">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_1">截至各季稅前損<br/><span style="padding-left: 69px;">益財測達成情形</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t52sb01">年度自結稅前損<br/><span style="padding-left: 69px;">益(未經會計師</span><br/><span style="padding-left: 69px;">查核)達成情形</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t52sb02">年度實際稅前損<br/><span style="padding-left: 69px;">益(經會計師查</span><br/><span style="padding-left: 69px;">核)達成情形</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_2">各季稅前損益財<br/><span style="padding-left: 69px;">測達成情形(簡</span><br/><span style="padding-left: 69px;">式)</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t06sf09_3">當季稅前損益經<br/><span style="padding-left: 69px;">會計師查核(核</span><br/><span style="padding-left: 69px;">閱)數與當季預</span><br/><span style="padding-left: 69px;">測數差異達百分</span><br/><span style="padding-left: 69px;">之十以上者，或</span><br/><span style="padding-left: 69px;">截至當季累計差</span><br/><span style="padding-left: 69px;">異達百分之二十</span><br/><span style="padding-left: 69px;">以上者(簡式)</span></a><br/>
								</span>
							</span>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005002002"/><a onclick="showhide('level-2005002002','img-2005002002')" target="_self" href="#">處記缺失情形</a><br/>
							<span style="display: none;" id="level-2005002002">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t52sc03_4">完整式處記缺失<br/><span style="padding-left: 69px;">情形</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t52sc03_3">簡式處記缺失情<br/><span style="padding-left: 69px;">形</span></a><br/>
								</span>
							</span>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005002003"/><a onclick="showhide('level-2005002003','img-2005002003')" target="_self" href="#">財務預測相關資訊</a><br/>
							<span style="display: none;" id="level-2005002003">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sc02">完整式</a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sc02_1">簡式</a><br/>
								</span>
							</span>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="finance_w1">上市公司各季財測<br/><span style="padding-left: 52px;">彙總資料</span></a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005002005"/><a onclick="showhide('level-2005002005','img-2005002005')" target="_self" href="#">期間別財測公告情<br/><span style="padding-left: 52px;">形</span></a><br/>
							<span style="display: none;" id="level-2005002005">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t56sb02n_1_all">完整式財務預測<br/><span style="padding-left: 69px;">彙總查詢</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t56sball_1">簡式財務預測彙<br/><span style="padding-left: 69px;">總查詢</span></a><br/>
								</span>
							</span>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2005002006"/><a onclick="showhide('level-2005002006','img-2005002006')" target="_self" href="#">合併財務預測相關<br/><span style="padding-left: 52px;">資訊</span></a><br/>
							<span style="display: none;" id="level-2005002006">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sc02c">完整式</a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sc02_1c">簡式</a><br/>
								</span>
							</span>
						</span>
					</span>
				</span>
			</span>

		<img src="images/minus3.gif" id="img-2006"/>
			<a onclick="showhide('level-2006','img-2006')" target="_self" href="#">公告</a><br/>
			<span style="display: none;" id="level-2006">
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t67sb07">取得或處分資產公告</a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t116sb02">取得或處分私募有價<br/><span style="padding-left: 35px;">證券公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t100hsb05">董事會議決事項未經<br/><span style="padding-left: 35px;">審計委員會通過或獨</span><br/><span style="padding-left: 35px;">立董事有反對或保留</span><br/><span style="padding-left: 35px;">意見公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t138sb01">自結損益公告</a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t132sb16">公開發行股票全面轉<br/><span style="padding-left: 35px;">換無實體發行公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t06hsb07">財務報告無虛偽或隱<br/><span style="padding-left: 35px;">匿聲明書公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t06hsb09">會計主管不符資格條<br/><span style="padding-left: 35px;">件調整職務公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t108sb08_1_q1">轉換(附認股權)公司<br/><span style="padding-left: 35px;">債公告</span></a><br/>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t127sb00_q1">普通公司債暨金融債<br/><span style="padding-left: 35px;">券公告</span></a><br/>
				</span>


				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2006011"/>
					<a onclick="showhide('level-2006011','img-2006011')" target="_self" href="#">海外公司債公告</a><br/>
					<span style="display: none;" id="level-2006011">
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t47sb03_q6">海外一般公司債</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t47sb03_q7">海外轉換公司債</a><br/>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t47sb03_q8">海外附認股權公司<br/><span style="padding-left: 52px;">債</span></a><br/>
						</span>
					</span>
				</span>

				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t144sb02">分離後認股權憑證之<br/><span style="padding-left: 35px;">公告</span></a><br/>
				</span>
				
			</span>
		<img src="images/minus3.gif" id="img-2007"/>
			<a onclick="showhide('level-2007','img-2007')" target="_self" href="#">營運概況</a><br/>
			<span style="display: none;" id="level-2007">
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2007001"/>
					<a onclick="showhide('level-2007001','img-2007001')" target="_self" href="#">每月營收</a><br/>
					<span style="display: none;" id="level-2007001">

						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t21sc04_ifrs">採用IFRSs後每月<br/><span style="padding-left: 52px;">營業收入彙總表</span></a><br/>
						</span>

						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2007001001"/><a onclick="showhide('level-2007001001','img-2007001001')" target="_self" href="#">採用IFRSs前營業<br/><span style="padding-left: 52px;">收入彙總表</span></a><br/>
							<span style="display: none;" id="level-2007001001">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sc04">每月營業收入統<br/><span style="padding-left: 69px;">計彙總表</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t21sb06">每月合併營業收<br/><span style="padding-left: 69px;">入統計彙總表</span></a><br/>
								</span>
							</span>
						</span>

						<span style="padding-left: 35px;">
							<img src="images/pointer.gif"/><a target="_self" href="t05st08_all">各項產品業務營收<br/><span style="padding-left: 52px;">統計彙總表</span></a><br/>
						</span>
					</span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/minus3.gif" id="img-2007002"/><a onclick="showhide('level-2007002','img-2007002')" target="_self" href="#">財務比率分析</a><br/>
					<span style="display: none;" id="level-2007002">
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2007002001"/><a onclick="showhide('level-2007002001','img-2007002001')" target="_self" href="#">採IFRSs後</a><br/>
							<span style="display: none;" id="level-2007002001">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t51sb02_q1">財務分析資料查<br/><span style="padding-left: 65px;">詢彙總表</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t163sb06">營益分析查詢彙<br/><span style="padding-left: 69px;">總表</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t163sb07">毛利率彙總表</a><br/>
								</span>
							</span>
						</span>
						<span style="padding-left: 35px;">
							<img src="images/minus3.gif" id="img-2007002002"/><a onclick="showhide('level-2007002002','img-2007002002')" target="_self" href="#">採IFRSs前</a><br/>
							<span style="display: none;" id="level-2007002002">
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t51sb02">財務分析資料查<br/><span style="padding-left: 65px;">詢彙總表</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t51sb06">營益分析查詢彙<br/><span style="padding-left: 65px;">總表</span></a><br/>
								</span>
								<span style="padding-left: 52px;">
									<img src="images/pointer.gif"/><a target="_self" href="t51sb05">毛利率彙總表</a><br/>
								</span>
							</span>
						</span>
					</span>
				</span>
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t05st16_all">投資海外子公司資訊<br/><span style="padding-left: 30px;">彙總表</span></a><br/>
				</span> 
				<span style="padding-left: 15px;">
					<img src="images/pointer.gif"/><a target="_self" href="t92sb05">赴大陸投資資料查詢彙<br/><span style="padding-left: 30px;">總表</span></a><br/>
				</span>
			</span>

		<img src="images/pointer.gif"/><a href="t51sb01_1">下市/下櫃/撤銷登錄興櫃/<br/><span style="padding-left: 15px;">不繼續公開發行彙總表</span></a><br/>

		<img src="images/pointer.gif"/><a href="edco_w">初次上市(櫃)公司(IPO)穩<br/><span style="padding-left: 15px;">定價格措施</span></a><br/>

		<img src="images/pointer.gif"/><a href="t116sb01_new">辦理私募之應募人為內部<br/><span style="padding-left: 15px;">人或關係人</span></a><br/>
		
	</td>
</tr>
</table>


</div>
</td><td valign="top">

<div id='sw'><div id='pic' name="pic"  hspace="0" vspace="0" border="0" align="top" style="cursor: hand; background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 324px; width:14px;background-position:-542px 0px;" onclick="closex();"></div></div>
</td><td valign="top">
<div id="nav02">
<div class="t0"></div>
<div class="t01" id='caption'><br>&nbsp;&nbsp;&nbsp;綜合損益表</div>
<div id="bar01">

<form id="form1" name="form1" action="/mops/web/ajax_t163sb04" onsubmit="return false;" method="post">
<input type="hidden" id="subMenuID" value="[2,2004,2004001]">

<table width="775" border="0" cellpadding="0" cellspacing="0" >
<tr>
	
	<td class="bar01a" valign="top" width="6px"><div style="background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 52px; width:6px;background-position:1px 0px;"></div></td>
	<td class="bar01b" valign="top"><!-- 市場別, 年度, 季別 -->
		<input type="hidden" name="step" value="1">
		<input type="hidden" name="firstin" value="ture">
		<input type="hidden" name="off" value="1">
		<input type="hidden" name="isQuery" value="Y">
		<table border="0" cellspacing="0" cellpadding="2">
		<tr>
			<td><div id="div4" style="background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 11px; width:11px;background-position:-345px 0px;"></div></td><td>市場別</td>
			<td><div id="search_bar1">
				<div class="search">
					<select id="TYPEK" name="TYPEK"><option value="sii">上市</option><option value="otc">上櫃</option><option value="rotc">興櫃</option><option value="pub">公開發行</option></select>
				</div>
			</div></td>
			<td><div id="div4" style="background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 11px; width:11px;background-position:-345px 0px;"></div></td><td>年度</td>
			<td><div id="search_bar1">
				<div class="search">
					<input name="year" type="text" class="textbox" id="year" value="" size="3" maxlength="3" onkeydown="{if(event.keyCode==13){document.getElementById('season').focus(); return false;}}"/> 
				</div>
			</div></td>
			<td><div id="div4" style="background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 11px; width:11px;background-position:-345px 0px;"></div></td><td>季別</td>
			<td><div id="search_bar1">
				<div class="search">
					<select name="season" id="season">
						<option value=""></option>
						<option value="01">1</option>
						<option value="02">2</option>
						<option value="03">3</option>
						<option value="04">4</option>
					</select>
				</div>
			</div></td>
		</tr>
		</table>
</td>
	<td align="right" class="bar01b">&nbsp;</td>
	<td align="right" class="bar01b" valign="top">
		<table border="0" cellspacing="0" cellpadding="2">
		<tr>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td><div id="search_bar1">
				<div class="search">
				
				
				<input type="button" value=" 查詢 " onclick="javascript:doAction();ajax1(document.form1,'table01');"/>
				</div>
			</div></td>
		</tr>
		</table>
	</td>
	
	<td class="bar01a" valign="top" width="6px"><div style="background: url(images/map2.gif) no-repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; height: 52px; width:6px;background-position:-72px 0px;"></div></td>
</tr>
</table>
</form>

</div>


<div id="table_ess">
  <table id="showTable9" border="0" cellspacing="0" cellpadding="2">
    <tr>
      
      
	  <th align="left" width="80px"><a href="javascript:outputNewWindowPrint();"><img src="images/bu_01.gif" alt="列印網頁" border=0></img></a></th><th width="80px"><a href="javascript:outputNewWindow();"><img src="images/bu_02.gif" alt="開新視窗" border=0></img></a></th><th width="80px"><a href="javascript:reportError();"><img src="images/bu_04.gif" alt="問題回報" border=0></img></a></th><th width="80px"><a id='ajax_back_button' href="javascript:void(0)" onclick="ajax_back();" style="visibility:hidden;"></a></th>
      <th><table border="0" cellspacing="0" cellpadding="0">
        <tr>
           
		  <td width="650px"></td>
        </tr>
      </table></th>
    </tr>
  </table>
</div>
<div id="zoom"><div id="table01"




></div>
  <br></div>
</td></tr></table>
</DIV></tr>
</table>
</div>


<div id="footer">
   <table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <th>
		<div class="text1" id="text1" align="center">
			<a href='https://www.stockvote.com.tw/' target='_blank'>電子投票</a>│
			<a href='http://www.sfb.gov.tw/Layout/main_ch/index.aspx?frame=5' target='_blank'>不繼續公開發行</a>│
			<a href='/server-java/t39sb01' target='_blank'>市場公告</a>│
			
			
			<a href='https://www.sfi.org.tw/cga/cga1' target='_blank'>公司治理評鑑</a>│


			
			
			
			<a href='/mops/web/t146sb08'>網站地圖</a>│
			<a href='/nas/MOPS_HandBook.doc' target='_MOPS_handbook'>網站使用說明</a>
			<div class="text1" id="text1" align="center" height="80">
			<a href=#>投資人服務中心(02)2792-8188</a> <u><a href='http://Suggestionbox.twse.com.tw' target='_blank'>聯絡我們</a></u>
			</div>

			
			
			
			
			
			
			
			
		</div>
	</th>
  </tr>
</table>
</div>
</td></tr></table></center>
<div id="quicksearch9" style="position:absolute;z-index:3;overflow:auto;width:620px;max-height:200px;display:none;"></div>
</body>


<script>
function doAction() {
	if (document.form1.step!=null && document.form1.step!=undefined && document.form1.step.value!='')
	{
		if (document.form1.step.value!='0')
		{
			document.form1.step.value='1';
		}
	}
	if (document.form1.firstin!=null && document.form1.firstin!=undefined && document.form1.firstin.value!='')
	{
		document.form1.firstin.value='1';
	}
	var name=document.fh.funcName.value;
	document.form1.action='/mops/web/ajax_'+name;
}
function checkAutoRunScript(){
	if (document.autoForm!=null && document.autoForm!=undefined && document.autoForm.run.value==''){
		document.autoForm.run.value='Y';
		ajax1(document.autoForm,'table01');
	}

	if (document.autoRunScript!=null && document.autoRunScript!=undefined && document.autoRunScript.run.value!=''){
		var s = document.autoRunScript.run.value;
		document.autoRunScript.run.value = '';
		new function(){
			eval(s);
		};
	}

}

setInterval("checkAutoRunScript()",100);
</script>
</html> '''
soup=BeautifulSoup(data,'lxml')
print(soup.prettify())
print(soup.head)
print(soup.title.string)

print(soup.get_text())
print(soup.find_all('span'))
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.title)
print(soup.find('a'))
print(soup.find('b'))
# soup=soup.select('.span')
# print(web.get('href'))

# print(soup.find_all('a',{'onclick':"showhide('level-2004','img-2004'"}))

# for c in soup.find_all('span'):
#         print(c.get('class'))
        
# print(soup.title.string)
# s='http://www.tpex.org.tw/web/stock/aftertrading/daily_turnover/trn_result.php?l=zh-tw&t=D'
# r=requests.get(s)
# hl=r.text.splitlines()
# k=input()
# for row in hl:
#     if k in row:
#         n+=1
# print(k,n)        
        

# print(r.status_code)
# re=r.headers
# print(re)
# data=r.json()
# print(data['success'])
# print(data['result'])
# res=ur.urlopen('https://mops.twse.com.tw/mops/web/t163sb04')
# url='https://mops.twse.com.tw/mops/web/t163sb04'
# html_body=requests.get(url)
# html_body.encoding='utf8'
# print(html_body.text)

# c=res.read()
# print(c)
# print(res.status)
# print(res.getheaders())

# print('',c.decode())
# print(res.status)

import re
p=re.compile(r"\d+")
r1=p.findall('tsm23302303umc')
r2=p.findall('tsm2330evergreen2303umc',0,10)
print(r2)
k='evergreen.all.in.2603'
p1='.+.'
p2=re.compile(p1)
print(p2.findall(k))
p1='@.?+\.'
p2=re.compile(p1)
print(p2.findall(k))