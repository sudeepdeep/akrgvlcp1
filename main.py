<!DOCTYPE html>
<html>
<head>
	<title>Home Page</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
	body{
		background-color: white;
	}
	.logo img{
		width:80%;
		height:120px;
	}

 .heading{
		font-family: cursive;
		background-color: #031458;
		  color:white;
		  
		   
		    
	}

	#myBtn {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 99;
  font-size: 18px;
  border: none;
  outline: none;
  background-color: transparent;
  color: red;
  cursor: pointer;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 6px 6px rgba(0, 0, 0, 0.6);
}

#myBtn:hover {
  background-color: transparent;
}

.splash{
			position: fixed;
			top: 0;
			left: 0;
			height: 100vh;
			width: 100vw;
			background-color: #10B4FC;
			font-size: 2em;
			display: flex;
			align-items: center;
			justify-content: center;
			animation-name: open;
			animation-delay:3.5s;
			animation-duration: 2s;
			animation-fill-mode: forwards;
		}
		.splash img{
			z-index: 9;
		}
		.splash::after, .splash::before{
			content: "";
			position: absolute;
			background-color: #10B4FC;
			height: 100vh;
			width: 300vw;
			z-index: 99;
			animation-name: open;
			animation-fill-mode: forwards;
			animation-duration: 3s;
		}
		.splash after{
			left:30vw;
			animation-delay: 200ms;
		}
		.splash before{
			left: 0;
			animation-delay: 2s;
		}
		@keyframes open{
			0%{
				transform: translate(0, 0);
			}
			100%{
				transform: translate(100%, 0);
			}
		}
@media screen and (max-width: 1060px) {
.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	height: 120px;
}
}
@media screen and (max-width: 1018px) {
	.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	padding-top: 10px;
	
	
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 28px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 200px;
	width: 200px;
}
}

@media screen and (max-width: 768px) {
	.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	height: 120px;
	
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 25px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 160px;
	width: 160px;
}
}
@media screen and (max-width: 668px) {
	.logo img{
	width: 80%;
	height: 120px;

}
 .heading{
	color:white;
	height: 120px;
	text-align: center;
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 23px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 140px;
	width: 140px;
}
}
@media screen and (max-width: 568px) {
	.logo img{
	width: 90%;
	height: 100px;
	margin-left:0px; 

}
.heading{
	width:100%;
	height: 100px;
}
.heading h1{
	color:white;
	font-size: 25px;	
	text-align: center;

}
.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 20px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}


marquee img{
	height: 120px;
	width: 120px;
}
}
@media screen and (max-width: 548px) {
	.logo img{
		width: 80%
		height: 100px;
	margin-left:0px; 

}
.heading{
	width:100%;
	height: 100%;

	
}
.heading h1{
	color:white;


	
	
}
.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 20px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 100px;
	width: 100px;
}	

}



</style></head>
<body>
<div class = "splash">
	<img src = "{{url_for('static',filename = 'images/gifmaker.gif')}}">
</div>
<div class = "container">
		<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>



<script>
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
</script>
<table width="100%">
	<tr>
		<td colspan  = "2" align="center" width="100%">
			<div class = "logo">
			<img src = "{{url_for('static',filename = 'images/unnamed.png')}}"></div>
		</td>
	</tr>
	<tr>
		<td colspan  = "2" align="center" width="100%" style="background-color: #031458;">
			<div class = "heading">
			<h1>Welcome to the Virtual lab of <br>AKRG CET</h1></div>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="50px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width = "40%">
			<div class = "heading1">
			<h1 style="font-family:cursive; color:black;">Here you can perform your Lab Works from Home!!
			We are providing different compilers to work 
				on your lab assignments and to finish your programs</h1></div>
		</td>

		<td align="center" width="60%">
			<div class = "image2">
			<img src = "{{url_for('static',filename = 'images/student.jpg')}}" width="60%"></div>
		</td>

	</tr>

	<tr>
		<td colspan="2" align="center">
			<h1 style="font-family:candara; color:#031458;">Available Compilers</h1>
		</td>
	</tr>
	
	<tr>
		<div class = "inside">
		<td align="center" width="50%">
			<a href = "/c" ><img src = "{{url_for('static',filename = 'images/cc.png')}}" 	width="30%;"></a>

		</td>
		<td  align="center" width="50%">
			<a href = "/c1"><img src = "{{url_for('static',filename = 'images/c+++.png')}}" width="25%;" ></a>
			
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/python"><img src = "{{url_for('static',filename = 'images/python.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/java"><img src = "{{url_for('static',filename = 'images/java1.png')}}" width="30%;" ></a>
		</td>
	</tr>
<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/ds"><img src = "{{url_for('static',filename = 'images/ds.png')}}"  width="40%"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/ads"><img src = "{{url_for('static',filename = 'images/ads.png')}}" width="30%;" ></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/htm"><img src = "{{url_for('static',filename = 'images/html.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/sql"><img src = "{{url_for('static',filename = 'images/sql2.png')}}" width="30%;" ></a>
		</td>
	</tr>
<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/ml"><img src = "{{url_for('static',filename = 'images/ml.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/rp"><img src = "{{url_for('static',filename = 'images/rp.png')}}"  width="30%;" ></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/nix"><img src = "{{url_for('static',filename = 'images/nix.png')}}" width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "#"></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr></div>

<tr><td colspan="2" width="100%" align="center">
<h2 style="font-size: 20px;">To Submit your assingment Please <a href = " https://mail.google.com/mail/u/0/#inbox?compose=CllgCJZXhcwTsHSHBNMPhzvKghKlClmNMTQLBzJmXKXzmRqQWBkQkGWfGllLgtgchSDPXPwDhXV" target="_blank">Click Here</a></h2></td></tr>

<tr><td colspan="2" width="100%" >

<label style="font-size: 20px; font-family: candara; color: black;">Sincere thanks to </label></td></tr>
<tr><td colspan="2" width="100%">
<marquee >

	<a href = "https://www.programiz.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/pz.png')}}"></a>
	<a href = "https://www.javatpoint.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/javatpoint.png')}}" width="300px" height="250px;"></a>
	<a href = "https://www.onlinegdb.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/online.png')}}" width="300px" height="250px;"></a>
	<a href = "https://paiza.io/en" target="_blank"><img src = "{{url_for('static',filename = 'images/paiza.png')}}" width="300px" height="250px;"></a>
</marquee></td></tr>
<tr><td colspan="2" width="100%" align="center">
<footer style=" color: white;font-family: candara;font-size: 20px;background-color: #031458; padding-top: 20px; padding-bottom: 20px;">©CopyRight By CSE Students(2k17 - 2021)</footer></td></tr>
</table></div>
</body>
</html>
