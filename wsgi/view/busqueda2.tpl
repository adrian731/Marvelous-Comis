%include('header.tpl')
	<h1><font COLOR=yellow>Looking for comics?.</font></h1>
	<form class="form-container" action=/resultado2 method="post">
	<p>Insert a Marvel's character: <input name="name" type="text" class="search-field"/></p>
	<form class="form-container" action=/resultado2 method="post">
	<p>Insert another Marvel's character: <input name2="name2" type="text" class="search-field"/></p>
	<div class="submit-container">
	<input type="submit" value="Buscar" class="submit" />
	</div>
%include('footer.tpl')
