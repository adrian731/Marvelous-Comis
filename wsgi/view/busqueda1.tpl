%include('header.tpl')
	<body> 
	<h1><font COLOR=white>Buscar perfil de un jugador de Steam en concreto mediante su "NICK"</font></h1>
	<h2><font COLOR=white>Busca su NICK : <a href="https://steamcommunity.com/search/users">Aqui</a><font COLOR=white> 
	<div id="search-form">
	<form class="form-container" action="/resultadoperfil2" method="post">
	<p>NICK: <input name="nick" type="text" class="search-field"/></p>
	<div class="submit-container">
	<input type="submit" value="Buscar" class="submit" />
	<input type="reset" value="Restablecer" name="B2">
	</div>
	</body>
%include('footer.tpl')
