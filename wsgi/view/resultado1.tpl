%include('header.tpl')
		<table>
		%for x,y,z in zip(img,url,idcomic):
			<tr>
			<td><img src="{{x}}"/></td>
			<td>{{y}}</td>
			<td>{{z}}</td>
			<tr>
		%end
		</table>
%include('footer.tpl')
