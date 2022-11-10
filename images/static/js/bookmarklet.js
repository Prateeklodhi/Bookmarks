const siteurl = '//127.0.0.1:8000';
const styleurl = siteurl+ 'static/css/bookmarklet.css';
const minWidth = 250;
const maxHeight = 250;
//load css
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = siteurl+'?r='+Math.floor(Math.random()*9999999999999999);
head.appendChild(link); 
//load html
var body = document.getElementsByTagName('body')[0];
boxHtml = '<div id ="bookmarklet"><a href = "#" id ="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';

function bookmarkletLaunch(){
    bookmarklet - document.getElementById('bookmarklet');
    var imageFound = bookmarklet.querySelector('.images');
    //clear images found
    imageFound.innerHtml ='';
    bookmarklet.style.display = 'block';
    //cloase envent
    bookmarklet.querySelector('#close').addEventListener('click',function(){
        bookmarklet.style.display='none'
    });
}
bookmarkletLaunch();
 