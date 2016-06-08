%include('header.tpl')
		<table>
		%for x,y,z in zip(img,url,idcomic):
			<tr>
			<td><a href="{{y}}"><img src="{{x}}"/></a></td>
			
			<td>{{z}}</td>
			<tr>
		%end
		</table>
%include('footer.tpl')
