%include('header.tpl')
	<body> 
	<h1><font COLOR=white>Buscar el nombre de un personaje de Marvel.</font></h1>
	<form class="form-container" action="/resultadoperfil2" method="post">
	<p>NICK: <input name="nick" type="text" class="search-field"/></p>
	<div class="submit-container">
	<input type="submit" value="Buscar" class="submit" />
	<input type="reset" value="Restablecer" name="B2">
	</div>
	</body>
%include('footer.tpl')
