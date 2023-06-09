
var CourseHanziArray;//只有Hanzi 欄位的值
/* var CourseHanziArray = JSON.parse(sessionStorage.getItem('CourseHanziArray')); */ //抓取SelectCourse.html傳來的漢字資料 非使用django 方式
var AllHanzi; //此課程生字 從CourseHanziArray取得
let Hanzi_index = 0;//課程生字的陣列位置
var screenWidth; // 獲取螢幕寬度
var screenHeight; // 獲取螢幕高度
var svgWidth; //設定AllHanzi-container svg的寬
var svgHeight;//設定AllHanzi-container svg的高
//設定 
var VarAnimationspeed  //設定動畫播報速度
var VarshowHintAfterMisses //設定錯誤次數提示
var VardrawingWidth //設定畫筆大小
var Varrate; //設定播報語音rate


//請勿動 筆順練習時需要以下數值來讀取繪畫筆畫位置 。
function printStrokePoints(data) {
  var pointStrs = data.drawnPath.points.map((point) => `{x: ${point.x}, y: ${point.y}}`);
  /* console.log(`[${pointStrs.join(', ')}]`); */
}




window.onload = function () {


  //================容器縮小====================================
  //讓整個容器能縮小 and 更新筆順練習區塊
  var element = document.getElementById('cotainerallDiv');//使用div將需要縮小的區塊包起來。必須將element的高寬放置adjust外，避免重新抓值，造成無法縮小。
  var elementWidth = element.offsetWidth;
  var elementHeight = element.offsetHeight;
  var originalScale = 1; // 假設原始縮放比例為 1
  function adjustElementSize() {
    //console.log('Element Width:', elementWidth, 'Element Height:', elementHeight);
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    //console.log('Window Width:', windowWidth, 'Window Height:', windowHeight);
    var scale = Math.min(windowWidth / elementWidth, windowHeight / elementHeight);

    if (scale > originalScale) {
      // 視窗放大，使用原始縮放比例
      scale = originalScale;
      
    }

    element.style.transform = 'scale(' + scale + ')';
    console.log('Scale:', scale);
    updateCharacter();//重新讓筆順練習背景更新
  }

  // 在窗口加載時和窗口大小改變時執行調整函式
  window.addEventListener('load', adjustElementSize);
  window.addEventListener('resize', adjustElementSize);
  //================容器縮小====================================

  CourseHanziArray = HanziCourseArray //抓取課程生字，從views傳來的值
  AllHanzi = CourseHanziArray;//將陣列內容值，給予AllHanzi
  console.log(AllHanzi);
  /* console.log(CourseHanziArray); */
  setTimeout(function () {
        $(document).ready(function () {
            document.getElementById("loader").style.display = "none"; //載入區塊隱藏
            document.getElementById("myDiv").style.display = "block";//內容區塊 開啟
            updateCharacter();//避免筆順練習區塊 抓不到value
        });
     }, 800);
     
    CourseAllHanzi();//取得此課程的所有漢字
    updateCharacter();//更新 如有變動工具列數值等等
    getData();//漢字 部首 注音
    AllHintStroke();
    SettingUpdateValue();
    speechSynthesis.cancel(); // stop speaking
    document.querySelector('#animation').addEventListener('click', function () {
      /* target.classList.remove('pen-icon');//移除鼠標樣式 */
      /* VarAnimationspeed = document.querySelector('[name="Animationspeed"]').value; //繪畫速度 */
      
      /* console.log(Animationspeed); */
      updateCharacter();
      getData();
      writer.animateCharacter();
      /* HiddenCanvas(); */
    });
    

    //按下進階練習
    document.querySelector('.js-hardquiz').addEventListener('click', function (){
      CanvasHanziBg(AllHanzi[Hanzi_index]);
    });
    
    //按下筆順練習按鈕
    document.querySelector('#generally').addEventListener('click', function () {
    Toasty();//跳出Toasts
    updateCharacter();
    let i=1;
    var CompleteMsg='';//筆順練習完成提示訊息
    
    var opts = {
      onMistake: function(strokeData) {
        console.log('目前第'+  (strokeData.strokeNum+i) +'筆畫錯誤。');
        console.log("你在這個筆劃上犯了 " + strokeData.mistakesOnStroke + " 個錯誤!");
        console.log("目前總共錯誤 " + strokeData.totalMistakes + " 次。");
        console.log("距離完成還有" + strokeData.strokesRemaining + "個筆畫。");
        console.log("");
      },
      onCorrectStroke: function(strokeData) {
        console.log('很好! 你畫的第' + (strokeData.strokeNum+i) + '筆畫是正確的!');
        console.log("你在這個筆劃上犯了 " + strokeData.mistakesOnStroke + " 個錯誤!");
        console.log("目前總共錯誤 " + strokeData.totalMistakes+ " 次。");
        console.log("距離完成還有" + strokeData.strokesRemaining + "個筆畫。");
        console.log("");
      },
      onComplete: function(summaryData) {
        CompleteMsg = 'Ya~你完成了! 你畫完' + summaryData.character +"這個字了";
        document.querySelector('.toast-body').innerHTML=CompleteMsg;
        console.log('Ya~你完成了! 你畫完' + summaryData.character +"這個字了");
        console.log("總共錯誤 " + summaryData.totalMistakes + " 次。");
        console.log("");
      }
    }
    writer.quiz(opts);
  });
  screenWidth = window.innerWidth; //螢幕寬度
  screenHeight = window.innerHeight; //螢幕高度
  svgWidth = screenHeight * 0.12; //設置課程的所有漢字SVG高度為螢幕寬度的12%
  svgHeight = screenHeight * 0.12;//設置課程的所有漢字SVG高度為螢幕高度的12%
};









//漢字筆順順序區塊(某個漢字的全部筆順) 右邊欄
function renderFanningStrokes(target, strokes) {
  var docs_target_div = document.getElementById("docs-target-HintAllstroke");
  var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.style.width = '80px';
  svg.style.height = '80px';
  svg.style.border = '1px solid black'
  svg.style.marginRight = '1px'
  svg.classList.add("docshanzi_Svg"); // 添加共同的 classname

  var group = document.createElementNS('http://www.w3.org/2000/svg', 'g');

  var transformData = HanziWriter.getScalingTransform(80, 80);
  group.setAttributeNS(null, 'transform', transformData.transform);
  svg.appendChild(group);

  strokes.forEach(function(strokePath) {
    var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttributeNS(null, 'd', strokePath);
    path.style.fill = '#555';
    group.appendChild(path);
  });
  
  docs_target_div.appendChild(svg); // 將 SVG 加到 div 內
  docs_target_div.appendChild(document.createElement("br"));
  docs_target_div.appendChild(document.createElement("br"));
}
function AllHintStroke(){
  document.getElementById("docs-target-HintAllstroke").innerHTML = '';
  HanziWriter.loadCharacterData(AllHanzi[Hanzi_index]).then(function(charData) {
    var target = document.getElementById('target');
    for (var i = 0; i < charData.strokes.length; i++) {
      var strokesPortion = charData.strokes.slice(0, i + 1);
      renderFanningStrokes(target, strokesPortion);
    }
  });
}

//進階測驗的漢字形狀畫布背景 非常重要
function CanvasHanziBg(char){
  HanziWriter.loadCharacterData(char).then(function(charData) {
    // create a new canvas element
    var canvas = document.getElementById('canvas');
    console.log(canvas.width+","+canvas.height);
    // get the 2d context of the canvas
    var ctx = canvas.getContext('2d');
  
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.width = canvas.width;
    svg.style.height = canvas.height;
    var group = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  
    // set the transform property on the g element so the character renders at 150x150
    var transformData = HanziWriter.getScalingTransform(canvas.width, canvas.height);
    group.setAttributeNS(null, 'transform', transformData.transform);
    svg.appendChild(group);
  
    charData.strokes.forEach(function(strokePath) {
      var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttributeNS(null, 'd', strokePath);
      // style the character paths
      path.style.fill = '#e4e4e4';//path中間填滿
      /* path.style.stroke = '#555'; *///path 邊框
      
      group.appendChild(path);
    });
  
    // draw the SVG onto the canvas
    var svgData = new XMLSerializer().serializeToString(svg);
    var img = new Image();
    img.src = 'data:image/svg+xml;base64,' + btoa(svgData);
    img.onload = function() {
      // set the canvas as the background of the target canvas element
      var target = document.getElementById('canvas');
      target.style.backgroundImage = 'url(' + canvas.toDataURL() + ')';
      ctx.fillStyle = "#fff"; /* canvas背景顏色 */
      ctx.fillRect(0, 0, canvas.width,canvas.height ); /* 大小 */
      ctx.drawImage(img, 0, 0);
      cPush(); //圖片 儲存至array中
    };
    
  });
}


//取得此課程的所有漢字 左邊欄  HanziWriter.loadCharacterData() 是非同步的函數
//此方法async/await 僅適用於現代瀏覽器 舊瀏覽器須注意
async function CourseAllHanzi() 
{
    var target = document.getElementById('AllHanzi-container'); //存放按下確定後的所有漢字的容器 div
    /* console.log(size); */
    for (var i = 0; i < AllHanzi.length; i++) {
      var charData = await HanziWriter.loadCharacterData(AllHanzi[i]);
      
      var hanziDiv = document.createElement('div');
      hanziDiv.className = 'Hanzi-container'; // 可以為這個div加上一個自定義的class名稱，以便您對它進行樣式設置
      target.appendChild(hanziDiv);
      
      var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.style.width = svgWidth;
      svg.style.height = svgHeight;
      svg.style.border = '1px solid black';
      svg.setAttribute('class', 'HanziSvg');
      svg.setAttribute('id', `HanziSvg_${i}`);
      hanziDiv.appendChild(svg);
  
      var group = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      // set the transform property on the g element so the character renders at 150x150
      var transformData = HanziWriter.getScalingTransform(svgWidth, svgHeight);
      group.setAttributeNS(null, 'transform', transformData.transform);
      svg.appendChild(group);
  
      hanziDiv.appendChild(document.createElement("br"));
      hanziDiv.appendChild(document.createElement("br"));
  
      charData.strokes.forEach(function(strokePath) {
        var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttributeNS(null, 'd', strokePath);
        // style the character paths
        path.style.fill = '#555';
        group.appendChild(path);
      });
    }
    let HanziSvg0 = document.getElementById('HanziSvg_0');
    HanziSvg0.style.border = '1px solid red';
}
/* 底下為統一在一個容器底下的code */
/* async function CourseAllHanzi() 
{
    var target = document.getElementById('tmp-svg'); //存放按下確定後的所有漢字 div
    for (var i = 0; i < AllHanzi.length; i++) {
      var charData = await HanziWriter.loadCharacterData(AllHanzi[i]);
      
      var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.style.width = 150;
      svg.style.height = 150;
      svg.style.border = '1px solid black';
      target.appendChild(svg);
  
      var group = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      // set the transform property on the g element so the character renders at 150x150
      var transformData = HanziWriter.getScalingTransform(150, 150);
      group.setAttributeNS(null, 'transform', transformData.transform);
      svg.appendChild(group);
  
      target.appendChild(document.createElement("br"));
      target.appendChild(document.createElement("br"));
  
      charData.strokes.forEach(function(strokePath) {
        var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttributeNS(null, 'd', strokePath);
        // style the character paths
        path.style.fill = '#555';
        group.appendChild(path);
      });
  
      
    }
  } */

  //筆順練習漢字背景、更新漢字設定等等
  function updateCharacter() {
    /* 取得筆順區塊大小 */
    const divElement = document.getElementById('StrokeBlock');
    const divWidth = divElement.clientWidth;
    const divHeight = divElement.clientHeight;
    /* console.log(divWidth,divHeight);
    console.log(divElement2.clientWidth , divElement2.clientHeight); */
    document.querySelector('#target').innerHTML = '';
    SettingUpdateValue();
    //筆順練習漢字背景
    writer = HanziWriter.create('target', AllHanzi[Hanzi_index], {
      width: divWidth,
      height: divHeight,
      renderer: 'svg',
      onCorrectStroke: printStrokePoints,
      onMistake: printStrokePoints,
      radicalColor: '#166E16',//部首顏色
      showCharacter: false,
      strokeAnimationSpeed: VarAnimationspeed, //繪製筆畫速度
      strokeHighlightSpeed: 0.45, //提示筆畫速度
      highlightColor: '#ffa500',//提示顏色
      showHintAfterMisses: VarshowHintAfterMisses, 
      drawingWidth: VardrawingWidth, //繪製筆寬度 
    });
    isCharVisible = true;
    isOutlineVisible = true;
    window.writer = writer;
  }

///===========小功能列=======================
//更新所設定之值 (播報速度、動畫速度、錯誤次數提示、筆順粗細)
function SettingUpdateValue(){
  Varrate = document.querySelector('[name="rate"]').value;
  VarAnimationspeed = document.querySelector('[name="Animationspeed"]').value;
  VarshowHintAfterMisses = document.querySelector('[name = HintAfterMisses]').value;
  VardrawingWidth = document.querySelector('[name = drawingWidth]').value;
  document.getElementById('customRange1txt').innerHTML=Varrate;
  document.getElementById('customRange2txt').innerHTML=VarAnimationspeed;
  document.getElementById('customRange3txt').innerHTML=VarshowHintAfterMisses;
  document.getElementById('customRange4txt').innerHTML=VardrawingWidth;
}

//AllHanzi-container
//被選擇到的框線 需變紅色
function HanziSvg_Activeborder(){
  var HanziSvg =document.getElementById( `HanziSvg_${Hanzi_index}`)
  HanziSvg.style.border = '1px solid red';
}
//復原框線顏色
function HanziSvg_Passiveborder() {
  var HanziSvg =document.getElementById( `HanziSvg_${Hanzi_index}`)
  HanziSvg.style.border = '1px solid black';
}

//使用箭頭來調整練習的漢字
function Previoushanzi()//按下 上一個 的按鈕 <=
{
  HanziSvg_Passiveborder();
  //如果是在第一個漢字 按下 "上一個箭頭"漢字就會到最後一個漢字
  if(Hanzi_index == 0)
  {
    Hanzi_index= AllHanzi.length-1
    /* console.log("到最後一個漢字"); */
  }
  else if(Hanzi_index>0)
  {
    Hanzi_index-=1;
  }
  /* console.log("目前是:"+Hanzi_index+"Prev"); */
  updateCharacter();
  getData();
  AllHintStroke();
  HanziSvg_Activeborder();
  speechSynthesis.cancel(); // stop speaking
  cPushArray.length = 0; //避免進階練習背景，跑到上一個漢字

}

function Nexthanzi()//按下 下一個 的按鈕 =>
{
  HanziSvg_Passiveborder();
  //如果是在最後一個漢字 按下 "下一個箭頭"漢字就會到第一個漢字
  if(Hanzi_index== AllHanzi.length-1){
    Hanzi_index=0
  }
  else if(Hanzi_index <AllHanzi.length)
  {
    Hanzi_index+=1;
  }
  /* console.log("目前是:"+Hanzi_index+"next"); */
  updateCharacter();
  getData();
  AllHintStroke();
  HanziSvg_Activeborder();
  speechSynthesis.cancel(); // stop speaking
  cPushArray.length = 0; //避免進階練習背景，跑到上一個漢字

}

//按下筆順練習 需要跳出Toasts
var option = 
{
    animation : true,
    delay : 2000
};
function Toasty()
{
      var toastHTMLElement = document.getElementById( 'EpicToast' );
      var toastElement = new bootstrap.Toast( toastHTMLElement, option );
      toastElement.show( );
}

///===========小功能列=======================


//=========語音播報 漢字資訊========================
const msg = new SpeechSynthesisUtterance();
let voices = [];
let options = [];
let speakButton;

window.addEventListener('load', function() {
  speakButton = document.querySelector('#speak');
  options = document.querySelectorAll('[type="range"], [id="customRange1txt"]');
  if (speakButton) {
    console.log('speak');
    speakButton.addEventListener('click', toggle);
  }

  function populateVoices(){
    voices = this.getVoices();
    console.log(voices);
    msg.lang = "zh-TW"
  }

  // 觸發播放
  function toggle(startOver = true) {
    speechSynthesis.cancel(); // stop speaking
    if (startOver) {
      speechSynthesis.speak(msg); // restart speaking
    }
  }

  // 改變 utterance 的 rate 屬性的值
  function setOption() {
    if (this.name === 'rate') {
      console.log("成功");
      console.log(this.name, this.value);
      msg[this.name] = this.value;
      toggle();
      console.log(this.value);
      /* document.getElementById("customRange1txt").innerHTML = this.value; */
    }
  }

  speechSynthesis.addEventListener('voiceschanged', populateVoices);
  options.forEach(option => option.addEventListener('change', setOption));
});
//=========語音播報 漢字資訊========================



//==========取得漢字資訊 部首 筆畫=========================
function getData()
{
  msg.text='';
  var a = AllHanzi[Hanzi_index];
  // hanziDataJs為全部的欄位 0:漢字 1:注音 2:部首 3:部首注音 4:總筆畫
  var hanziDataArray = [[hanziDataJs[Hanzi_index].fields.Hanzi],[hanziDataJs[Hanzi_index].fields.Bopomofo],[hanziDataJs[Hanzi_index].fields.Radical],[hanziDataJs[Hanzi_index].fields.R_Bopomofo],[hanziDataJs[Hanzi_index].fields.Total_strokes]]; 

  //因某些部首念不出來或多音字，所以用其他詞替代
  const hanziMapping = {
    '載': '在',
  };
  const radicalMapping = {
    '疋': '舒',
    '辵': '輟',
    '宀': '眠',
    '攴' : '鋪',
  };
  const HanziVoice = hanziMapping[hanziDataArray[0]] || hanziDataArray[0];
  const RadicalVoice = radicalMapping[hanziDataArray[2]] || hanziDataArray[2];
  console.log(RadicalVoice);


  var hanziB_lastCharacter = hanziDataArray[1][0].charAt(hanziDataArray[1][0].length - 1); //判斷注音聲調 是否為第一聲 ，不判斷第一聲會省略不念
  let t='';
  if(hanziB_lastCharacter == '¯')
  {
    t='第一聲'+HanziVoice;
  }
  else{
    t=HanziVoice;
  }
  var msgData = HanziVoice + "," + RadicalVoice + "部, 注音:" +  hanziDataArray[1]+ ",,,"+ t + "共"  +hanziDataArray[4] + "畫, ";
  msg.text = msgData; //播報要說的文字

  // 將 hanziDataArray[2] 的值放入 radicalTd 元素
  document.getElementById('radicalTd').textContent = hanziDataArray[2];

  // 將 hanziDataArray[1] 的值放入 bopomofoTd 元素
  document.getElementById('bopomofoTd').textContent = hanziDataArray[1];
  
  // 將 hanziDataArray[4] 的值放入 totalstrokeTd 元素
  document.getElementById('totalstrokeTd').textContent = hanziDataArray[4];
  /* console.log(Hanzi_docs) */
  /* text2 = "<table> <tr>";

  text2 += "<th bgcolor='transparent' colspan='2'>" +"部首"+"</th>";
  text2 += "<th bgcolor='transparent' colspan='2'>" +"注音"+"</th>";
  text2 += "<th bgcolor='transparent' colspan='2'>" +"總筆畫"+"</th>";

  text2 += "</tr><tr>";
  text2 += "<th colspan='2'>" + hanziDataArray[2] + "</th>";
  text2 += "<th colspan='2'>" + "<rt>" +  hanziDataArray[1] + "</rt>" + "</th>";
  text2 += "<th colspan='2'>" + hanziDataArray[4] + "</th>";
  text2 += "</tr></table>"; */
  /* document.getElementById("char-dictionary").innerHTML = text2; */
  /* xhr.open("GET", s, true);
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          var data = JSON.parse(xhr.responseText);
          var w_data = [data["title"], data["radical"], data["stroke_count"], data["heteronyms"][0]["bopomofo"]];
          var s = w_data[0] + ", " + w_data[1] + "部, " + "共" + w_data[2] + "畫, " + w_data[3]
          msg.text = s; //播報要說的文字
          if(w_data[1] == '{[8f54]}')//足部
          {
            const unicodeRadical = "8FB5"; // 該字的 Unicode 部首編碼
            const radicalChar = String.fromCodePoint(parseInt(unicodeRadical, 16));
            w_data[1]=radicalChar;
            console.log(radicalChar); // 顯示
          }
          else if(w_data[1] == '{[8ef3]}')
          {
            const unicodeRadical = "5E7F"; // 該字的 Unicode 部首編碼
            const radicalChar = String.fromCodePoint(parseInt(unicodeRadical, 16));
            w_data[1]=radicalChar;
            console.log(radicalChar); // 顯示
          }
          else if(w_data[1] == '{[fbfd]}')
          {
            const unicodeRadical = "5B80"; // 該字的 Unicode 部首編碼
            const radicalChar = String.fromCodePoint(parseInt(unicodeRadical, 16));
            w_data[1]=radicalChar;
            console.log(radicalChar); // 顯示
          }
          

          text2 = "<table> <tr>";

          text2 += "<th bgcolor='transparent' colspan='2'>" +"部首"+"</th>";
          text2 += "<th bgcolor='transparent' colspan='2'>" +"注音"+"</th>";
          text2 += "<th bgcolor='transparent' colspan='2'>" +"總筆畫"+"</th>";

          text2 += "</tr><tr>";
          text2 += "<th colspan='2'>" + w_data[1] + "</th>";

          text2 += "<th colspan='2'>" + "<rt>" +  w_data[3] + "</rt>" + "</th>";

          text2 += "<th colspan='2'>" + w_data[2] + "</th>";

          

          text2 += "</tr></table>";
          document.getElementById("char-dictionary").innerHTML = text2;
      }
  };
  xhr.send(); */
}

/* function get_Hanzidocs(){
  
  console.log(data[Hanzi_index].fields.Hanzi) ;
  console.log(data[Hanzi_index].fields.Bopomofo);
  console.log(data[Hanzi_index].fields.Radical);
  console.log(data[Hanzi_index].fields.Total_strokes);

} */


//=========進階練習=========================
var mousePressed = false;
var lastX, lastY;
var ctx;

function InitThis() {
  ctx = document.getElementById('canvas').getContext("2d");
  $('#canvas').mousedown(function (e) {
      mousePressed = true;
      Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
  });

  $('#canvas').mousemove(function (e) {
      if (mousePressed) {
          Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
      }
  });

  $('#canvas').mouseup(function (e) {
      if (mousePressed) {
          mousePressed = false;
          cPush();
      }
  });

  $('#canvas').mouseleave(function (e) {
      if (mousePressed) {
          mousePressed = false;
          cPush();
      }
  });
  drawImage();
}

//透過圖片的方式來存儲筆畫
function drawImage() {
  CanvasHanziBg(AllHanzi[Hanzi_index]);
  /* var canvasBg = document.getElementById('canvas');
  var dataURL = canvasBg.toDataURL();
  var img = new Image();
  img.src = dataURL;
  img.onload = function() {
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  }; */
}

//清除畫布按鈕
function confirmClear() {
  var confirmation = confirm("確定要清除所有筆畫嗎？");

  if (confirmation) {
    // 使用者選擇了確定清除
    drawImage();
  } else {
    // 使用者選擇了取消
  }
}



/* function drawImage() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'img/myimg.jpg', true);
  xhr.responseType = 'blob';
  xhr.onload = function() {
    if (this.status === 200) {
      var blob = this.response;
      var img = new Image();
      img.onload = function() {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        cPush();
      };
      img.src = URL.createObjectURL(blob);
    }
  };
  xhr.send();
} */

function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = $('#selColor').val();
        ctx.lineWidth = $('#selWidth').val();
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x; 
    lastY = y;
}
	

var cPushArray = new Array();
var cStep = -1;

//將目前所畫的筆劃存入array
function cPush() {
/*   console.log("11");
 */    cStep++;
    if (cStep < cPushArray.length) { cPushArray.length = cStep; }
    cPushArray.push(document.getElementById('canvas').toDataURL());

}
//上一個筆畫        
function cUndo() {
/*   console.log("22");
 */  if (cStep > 0) {
      cStep--;
      var canvasPic = new Image();
      canvasPic.src = cPushArray[cStep];
      canvasPic.onload = function () { ctx.drawImage(canvasPic, 0, 0); }

  }
}     
//下一個筆畫  
function cRedo() {
/*   console.log("33");
 */  if (cStep < cPushArray.length-1) {
      cStep++;
      var canvasPic = new Image();
      canvasPic.src = cPushArray[cStep];
      canvasPic.onload = function () { ctx.drawImage(canvasPic, 0, 0); }
    }
}

//下載圖片至桌面
function download(selector) {
  const canvas = document.querySelector(selector);
  
  // 将画布转换为数据 URL 并创建图像元素
  const dataURL = canvas.toDataURL('img/123.svg');
  const img = new Image();
  img.src =  dataURL;
  
  // 创建链接并下载
  const link = document.createElement('a');
  link.download = '您的姓名_'+AllHanzi[Hanzi_index];
  link.href =  dataURL;
  link.click();
  drawImage();
  /* CanvasHanziBg(AllHanzi[Hanzi_index]);
  ctx.putImageData(0, 0, 0); */
}
//=========進階練習=========================
